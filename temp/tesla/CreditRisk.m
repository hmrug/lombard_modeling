TSLA = readtable("C:\Study\Uni Basel\FS_21\applied credit model\TSLA.csv");
a_Hat = -1.87096;
b_Hat = -0.794554;
ADTV = mean(TSLA.Volume);
gamma = 10^a_Hat*ADTV^b_Hat;
epsilon = 0.01;
alpha = 0.25; %Margin Call
delta = 10; %10 business days to react to margin call
plot(TSLA.Date, TSLA.Close);
%Calculate daily return and standard deviation
numberDays = length(TSLA.Close);
logReturn  = log(TSLA.Close(2:end)./TSLA.Close(1:end-1));
mue = mean(logReturn);
sigma = std(logReturn); 
%Calculate the lending value
x=[0:1:100,200:100:10^4,2*10^4:10^4:10^6,2*10^6:10^6:10^8, 2*10^8:10^8:10^10];
lambda = (1-alpha).*exp(-x.*gamma + (mue-sigma^2/2)*delta+sigma*sqrt(delta)*norminv(epsilon))...
    ./(1-alpha.*exp(-x.*gamma + (mue-sigma^2/2)*delta+sigma*sqrt(delta)*norminv(epsilon)));
xx=1:numel(x);
plot(xx,lambda);
set(gca,'xtick',[0 101 200 299 398 497],'xticklabel',{'0','10^2','10^4', '10^6', '10^8', '10^10'});



