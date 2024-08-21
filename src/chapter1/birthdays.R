library(tidyverse)
threshold <- 2:5
ourData <- crossing(trial = 1:3000, people = 1:200) %>%
    mutate(birthday = map(people, ~ sample(365, ., replace = TRUE)),
           multiple = map_int(birthday, ~ max(table(.)))
          )

result <- ourData %>%
    crossing(threshold = 2:5) %>%
    group_by(people, threshold) %>%
    summarize(chance = mean(multiple >= threshold))

result %>%
    mutate(exact = map2_dbl(people, threshold,
                            ~ pbirthday(.x, coincident = .y))) %>%
    ggplot(aes(people, chance, color = factor(threshold))) +
    geom_line() +
    geom_line(aes(y = exact), lty = 2) +
    scale_y_continuous(labels = scales::percent_format()) +
    labs(x = "n",
         y = "Ratio",
         color = "k")


