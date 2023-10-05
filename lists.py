guests_invitation = ['Sarmad', 'Adil Altaf', 'Zia Khan']
print(f"{guests_invitation[0]}, you are invited for dinner")
print(f"{guests_invitation[1]}, you are invited for dinner")
print(f"{guests_invitation[2]}, you are invited for dinner")

print(guests_invitation[2])
guests_invitation[2] = "Hira khan"
print(f"{guests_invitation[0]}, you are invited for dinner")
print(f"{guests_invitation[1]}, you are invited for dinner")
print(f"{guests_invitation[2]}, you are invited for dinner")

print("Bigger table is found for dinner")
guests_invitation.insert(0, "Yonus")
guests_invitation.insert(0, "Ali")
guests_invitation.append("fahad")
print(guests_invitation)
print(f"{guests_invitation[0]}, you are invited for dinner.")
print(f"{guests_invitation[1]}, you are invited for dinner.")
print(f"{guests_invitation[2]}, you are invited for dinner.")
print(f"{guests_invitation[3]}, you are invited for dinner.")
print(f"{guests_invitation[4]}, you are invited for dinner.")
print(f"{guests_invitation[5]}, you are invited for dinner.")

print("I can invite only two people for dinner")
remove_peson_1 = guests_invitation.pop(0)
print(guests_invitation)
remove_peson_2 = guests_invitation.pop(0)
print(guests_invitation)
remove_peson_3 = guests_invitation.pop()
print(guests_invitation)
print(guests_invitation)
remove_peson_4 = guests_invitation.pop(0)
print(guests_invitation)
print(f"{remove_peson_1}, sorry you are not invited for dinner anymore.")
print(f"{remove_peson_2}, sorry you are not invited for dinner anymore.")
print(f"{remove_peson_3}, sorry you are not invited for dinner anymore.")
print(f"{remove_peson_4}, sorry you are not invited for dinner anymore.")
print(f"{guests_invitation[0]}, you are still invited for dinner")
print(f"{guests_invitation[1]}, you are still invited for dinner")
del guests_invitation[0]
del guests_invitation[0]
print(guests_invitation)

#List Sorting

cars:str = ['bmw', 'audi', 'toyota', 'sabaru']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars))
cars.reverse()
print(cars)
cars.reverse()
print(cars)
print(len(cars))