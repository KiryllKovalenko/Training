#лишил тащат топот радар
c = 'радара'
if c != c[::-1]: # -1 здесь шаг строки: от конца к началу
    print("It's not palindrome")
else:
    print("It's palindrome")