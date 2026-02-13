#strip() → removes spaces
# title() → capitalizes
# list comprehension → cleans all names
# lambda → condition
# filter() → removes small names

users = [" kumar ", "arun", " meena", "vi ", "divya "]
clean_users = list(
    filter(
        lambda name: len(name) > 4,
        [user.strip().title() for user in users]
    )
)
print(clean_users)
