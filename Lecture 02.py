u=[1,2,3,]
v=u.copy()

print(f"{u = }")
print(f"{v = }")

u[0]=9

print(f"{u = }")
print(f"{v = }")

u_list=[1,2,3]
u_tuple=(1,2,3)

print(u_list)
print(u_tuple)


x=dict(mode="batch", volume="3 L", initial_glucose=30, initial_ph=7.5)
print(x)
y={
    3: "Value 1",
    (3.0, 7.5): True,
    "mode": "batch",
    "volume": "3 L",
    "PID_active": ["T", "pH","DO"]
    }
print(y)

print(f"{x.keys()=}")
print(f"{x.values()=}")
print(f"{x.items()=}")

x=["Hi", 56, 793794, 985858]
for i in range(len(x)):
    print(f"{i}: {x[i]}")

    print()

    for x_item in x:
        print(x_item)

    for x_item in enumerate(x, start=1):
        print(f"{i}){x_item}")


for i in range (1, 11, 2):
    print (i)



x=[]
for i in range(10):
    x.append(i**2)

print(f"{x=}")

y=[i**2 for i in range(10)]
print(f"{x=}")

PH_MIN=6.5
PH_MAX=7.5
TEMP_MIN=36 #C
TEMP_MAX=38 #C

ph=7.05
temperature=37.0

if ph> PH_MAX:
    print("pH is too high. Injecting Acid...")
elif ph<PH_MIN:
    print("pH is too low. Injecting Base...")
else:
    print("pH is okay")

if temperature > TEMP_MAX:
    print("Temperature is too highe."
          "Increase cooling water flow rate...")
elif temperature < TEMP_MIN:
    print("Temperature is too low."
          "Decrease cooling water flow rate...")
else:
    print("Temperature is okay")

print("============")
ph_ok=(PH_MIN<= ph<= PH_MAX)
temperature_ok=(TEMP_MIN<= temperature<= TEMP_MAX)
print(f"{ph_ok=} and {temperature_ok=}")

if ph_ok and temperature_ok:
    print("Everything is okay :)")
