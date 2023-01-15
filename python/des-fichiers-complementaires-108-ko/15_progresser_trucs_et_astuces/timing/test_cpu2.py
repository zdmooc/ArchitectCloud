from timing import timing 

num_multiplies = 50000000
data = range(num_multiplies)
number = 1

with timing(label="Agaçons les cpus ") as t:
    for i in data:
        number *= 1.0000001

with timing(label="Agaçons les cpus ") as t:
    for i in data:
        number *= 1.0000001
        if not i % 10000000 and i>0 :
            t.tps_intermediaire(" %s " % i)

