# Kia and Hyundai Vehicle Theft Analysis
# Run from the project root directory.

knitr::opts_chunk$set(echo = TRUE)
# Load packages
library(readr)
library(readxl)
library(dplyr)
library(tidyr)
library(ggplot2)
library(lubridate)
library(treemapify)
library(scales)
library(stringr)

# Read data
kh <- read_csv("data/raw/kiaHyundaiThefts.csv",
               show_col_types = FALSE)
map_df <- read_csv("data/raw/carTheftsMap.csv",
               show_col_types = FALSE)
milwaukee <- read_csv("data/raw/KiaHyundaiMilwaukeeData.csv",
               show_col_types = FALSE)
raw_xlsx <- suppressMessages(read_excel("data/raw/Motherboard VICE News Kia Hyundai Theft Data.xlsx",
                       sheet = "Data",col_names = FALSE))

# Clean kiaHyundaiThefts.csv

# Clean Kia/Hyundai data
kh <- kh %>%
  mutate(
    month = str_trim(month),
    date = my(paste(month, year)),
    countKiaHyundaiThefts = parse_number(as.character(countKiaHyundaiThefts)),
    countOtherThefts = parse_number(as.character(countOtherThefts)),
    totalThefts = countKiaHyundaiThefts + countOtherThefts
  )

# Clean Milwaukee data
milwaukee <- milwaukee %>%
  mutate(
    month = str_trim(month),
    date = my(paste(month, year)),
    countKiaHyundaiThefts = parse_number(as.character(countKiaHyundaiThefts)),
    countOtherThefts = parse_number(as.character(countOtherThefts)),
    totalThefts = countKiaHyundaiThefts + countOtherThefts
  )

# Clean map data (removes coercion warnings)
clean_number <- function(x) {
  x <- str_trim(as.character(x))
  x[x %in% c("-", "NaN", "", "NA", "N/A")] <- NA
  parse_number(x)
}

map_df <- map_df %>%
  mutate(
    across(starts_with("countCarThefts"), clean_number),
    percentChange2019to2022 = clean_number(percentChange2019to2022)
  )


map_df <- map_df %>%
  mutate(
    change_group = case_when(
      percentChange2019to2022 < 0 ~ "Decrease",
      percentChange2019to2022 >= 0 & percentChange2019to2022 < 0.25 ~ "0% to 25%",
      percentChange2019to2022 >= 0.25 & percentChange2019to2022 < 1 ~ "25% to 100%",
      percentChange2019to2022 >= 1 ~ "100%+ Increase",
      TRUE ~ "Unknown"
    )
  )


city_names <- as.character(unlist(raw_xlsx[1, -1]))
city_names <- city_names[seq(1, length(city_names), by = 3)]
city_names <- city_names[!is.na(city_names)]

excel_list <- list()
col_index <- 2

for (city in city_names) {
  
  temp <- raw_xlsx[-c(1, 2), c(1, col_index, col_index + 1, col_index + 2)]
  
  names(temp) <- c("date", "kia_hyundai", "all_thefts", "percent")
  
  temp$city <- city
  
  excel_list[[city]] <- temp
  
  col_index <- col_index + 3
}

excel_long <- bind_rows(excel_list) %>%
  mutate(
    date = as.Date(date),
    kia_hyundai = clean_number(kia_hyundai),
    all_thefts = clean_number(all_thefts),
    percent = clean_number(percent)
  ) %>%
  filter(!is.na(date))



v1 <- excel_long %>%
  group_by(date) %>%
  summarise(total_kia_hyundai = sum(kia_hyundai, na.rm = TRUE))

ggplot(v1, aes(x = date, y = total_kia_hyundai)) +
  geom_area(alpha = 0.7, fill = "firebrick") +
  labs(
    title = "Growth of Kia/Hyundai Thefts Across 70 Cities Over Time",
    x = "Date",
    
    y = "Total Kia/Hyundai Thefts"
  ) +
   theme_minimal() +
  theme(
    plot.title = element_text(
      hjust = 0.5,
      face = "bold",
      size = 14
    )
  )


v2 <- kh %>%
  group_by(year) %>%
  summarise(
    kia_hyundai = sum(countKiaHyundaiThefts, na.rm = TRUE),
    other = sum(countOtherThefts, na.rm = TRUE)
  ) %>%
  pivot_longer(cols = c(kia_hyundai, other),
               names_to = "type",
               values_to = "count")

ggplot(v2, aes(x = year, y = count, fill = type)) +
  geom_area() +
  labs(
    title = "Kia/Hyundai Thefts vs Other Vehicle Thefts by Year",
    x = "Year",
    y = "Number of Thefts",
    fill = "Type"
  ) +
  theme_minimal() +
theme(
 plot.title = element_text(
   hjust = 0.5,
   face = "bold",
   size = 14
 )
)


v3 <- milwaukee %>%
  filter(year == 2022) %>%
  summarise(
    kia_hyundai = sum(countKiaHyundaiThefts, na.rm = TRUE),
    other = sum(countOtherThefts, na.rm = TRUE)
  ) %>%
  pivot_longer(cols = everything(), names_to = "type", values_to = "count") %>%
  mutate(
    fraction = count / sum(count),
    ymax = cumsum(fraction),
    ymin = lag(ymax, default = 0),
    label = percent(fraction)
  )

ggplot(v3, aes(ymax = ymax, ymin = ymin, xmax = 4, xmin = 2, fill = type)) +
  geom_rect() +
  coord_polar(theta = "y") +
  xlim(c(0, 4)) +
  labs(title = "Milwaukee 2022 Theft Composition") +
  theme_void() +
theme(
 plot.title = element_text(
   hjust = 0.5,
   face = "bold",
   size = 14
 )
)


v4 <- kh %>%
  group_by(city) %>%
  summarise(
    total_kia_hyundai = sum(countKiaHyundaiThefts, na.rm = TRUE),
    .groups = "drop"
  ) %>%
  arrange(desc(total_kia_hyundai))

ggplot(
  v4,
  aes(
    area = total_kia_hyundai,
    fill = total_kia_hyundai,
    label = city
  )
) +
  geom_treemap(color = "white") +
  geom_treemap_text(
    colour = "black",
    place = "centre",
    reflow = TRUE,
    grow = TRUE,
    size = 11
  ) +
  scale_fill_gradient(
    low = "#FEE8C8",    # light peach (lower theft)
    high = "#E34A33",   # dark orange-red (highest theft)
    name = "Theft Count"
  ) +
  labs(
    title = "Total Kia/Hyundai Thefts by City"
  ) +
  theme_minimal() +
  theme(
    plot.title = element_text(
      hjust = 0.5,
      face = "bold",
      size = 14
    )
  )


v5 <- kh %>%
  filter(year == 2022) %>%
  group_by(city) %>%
  summarise(
    kia_hyundai = sum(countKiaHyundaiThefts, na.rm = TRUE),
    other = sum(countOtherThefts, na.rm = TRUE)
  ) %>%
  mutate(total = kia_hyundai + other) %>%
  arrange(desc(total)) %>%
  slice_head(n = 10) %>%
  select(-total) %>%
  pivot_longer(cols = c(kia_hyundai, other),
               names_to = "type",
               values_to = "count")

ggplot(v5, aes(x = reorder(city, count, sum), y = count, fill = type)) +
  geom_bar(stat = "identity") +
  coord_flip() +
  labs(
    title = "2022 Vehicle Theft Mix in Top Cities",
    x = "City",
    y = "Theft Count",
    fill = "Type"
  ) +
  theme_minimal() +
theme(
 plot.title = element_text(
   hjust = 0.5,
   face = "bold",
   size = 14
 )
)


v6 <- kh %>%
  group_by(city) %>%
  summarise(
    total_thefts = sum(countKiaHyundaiThefts, na.rm = TRUE)
  ) %>%
  arrange(desc(total_thefts)) %>%
  slice_head(n = 5) %>%
  mutate(
    fraction = total_thefts / sum(total_thefts),
    ymax = cumsum(fraction),
    ymin = lag(ymax, default = 0),
    label = percent(fraction)
  )

ggplot(
  v6,
  aes(
    ymax = ymax,
    ymin = ymin,
    xmax = 4,
    xmin = 0,
    fill = city
  )
) +
  geom_rect(color = "white") +
  coord_polar(theta = "y") +
  xlim(c(0,4)) +
  labs(
    title = "Top 5 Cities Share of Kia/Hyundai Thefts",
    fill = "City"
  ) +
  theme_void() +
  theme(
    plot.title = element_text(
      hjust = 0.5,
      face = "bold",
      size = 14
    )
  )
  
