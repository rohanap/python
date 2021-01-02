guest_invitation = ['Emma','Sandra','Pamela','Julia']
hold_list = guest_invitation.pop()
hold_list1=guest_invitation.pop()
print(f"Sorry we cant invite you {hold_list} and {hold_list1}")
print(f"Guys you are on pending list {hold_list} and {hold_list1}")
guest_invitation.remove('Emma')
guest_invitation.remove('Sandra')
print(guest_invitation)