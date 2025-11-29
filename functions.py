def print_name(a):

    print(f"Hii,{a}")
    
def add(a, b):
    return (a+b)
add(2,3)

def student(** infos):
    for key, value in infos.items():
        print(key,":" ,value)
student(Name = "debojit",contact = 123)