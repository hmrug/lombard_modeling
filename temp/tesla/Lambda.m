function lambda = Lambda(alpha, gamma, mue, sigma, delta, epsilon, x)
lambda = (1-alpha).*exp(-x.*gamma + (mue-sigma^2/2)*delta+sigma*sqrt(delta)*norminv(epsilon))...
    ./(1-alpha.*exp(-x.*gamma + (mue-sigma^2/2)*delta+sigma*sqrt(delta)*norminv(epsilon)));
end 