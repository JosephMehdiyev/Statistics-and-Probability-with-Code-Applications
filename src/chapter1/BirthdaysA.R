n <- 1000;  m <- 50; e <- 0.05
s <- cumsum(2*(rbinom(n, size=1, prob=0.5) - 0.5))
plot(s/seq.int(n), type = "l", ylim = c(-0.4, 0.4))
abline(h = c(-e,e), lty = 2)
