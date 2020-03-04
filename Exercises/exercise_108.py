# Dictionary basics :D
#1 - Define a dictionary call story1, it should have the followign keys:
        # start, middle and end

story1 = {'start': 'Why did the chicken cross the road?',
          'middle': 'I don''t know',
          'end':'To get to the other side'}

#2 - Print the entire dictionary
print(story1)

#3 - Print the type of your dictionary
print(type(story1))

#4 - Print only the keys
print(story1.keys())

#4 - print only the values
print(story1.values())

#5 - print the individual values using the keys (individually, lots of printi commands)
print(story1['start'])
print(story1['middle'])
print(story1['end'])

#6 - Now let's add a new key:value pair.
    # 'hero': yourSuperHero

story1['epilogue'] = "Well thats not even funny..."
print(story1['epilogue'])