def args(name, *args):
    
    print(name, args)

def kwargs(**kwargs):

    for key,value in kwargs.items():

        print(key,value)


args("harsh",20,"new delhi")

kwargs(Name = "harsh", Age = 20, City = "new delhi")

