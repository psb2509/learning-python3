def life_expectancy(age,appl_eaten,cigs_smoke):
    life_ex=(100-age)+(appl_eaten*3.5) -(cigs_smoke*2)
    print(life_ex)

pradeep_data=[30,3,2];

# Regular argument passing .
life_expectancy(pradeep_data[0],pradeep_data[1],pradeep_data[2]);

# unpacking args
life_expectancy(*pradeep_data);