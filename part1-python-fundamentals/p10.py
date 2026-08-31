result = {
    "maths":75,
    "science":90,
    "english":50
}

print(max(result.values()))

print(max(result,key=result.get))

