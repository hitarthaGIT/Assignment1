'''If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
mile in minutes and seconds)? What is your average speed in miles per hour?'''

miles=10/1.61 
time_s=42*60+42  #time in seconds
time_m=42+(42/60) #time in minutes

tmp_m=time_m/miles #time per mile in minutes
tpm_s=time_s/miles  #time per mile in seconds

avg_speed=(miles/time_s)*3600
print(tpm_s,tmp_m,avg_speed)

# Output : 412.482 6.874700000000002  8.727653570337614


