library(tidyverse)
# R already has functions pnorm() to calculate what we need
x <- seq(-4, 4, 0.01) # to help plot c.d.f and p.d.f
y_pdf <- dnorm(x) # gives the p.d.f of Z
y_cdf <- pnorm(x) # gives the c.d.f of Z
data <- data.frame(x_value = x, y_value_pdf = y_pdf, y_value_cdf = y_cdf)
ggplot(data) +
    geom_line(aes(x = x, y = y_value_pdf, color = "p.d.f")) +
    geom_line(aes(x = x, y = y_value_cdf, color = "c.d.f")) +
    labs(title = "p.d.f and c.d.f of normal distribution", x = "X", y = "Value") +
    theme_minimal() 