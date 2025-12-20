from Package import maths

addi = maths.add(12, 12)
div = maths.division(12, 12)
mod = maths.modulas(12, 12)
multiple = maths.multiplication(12, 12)
sub = maths.substraction(12, 12)


print("Additon: ", addi)
print("Division: ", div)
print("moduls: ", mod)
print("multiplicatlion: ", multiple)
print("Substaraction: ", sub)




from Package import mean

me = mean.meean(12,13)
print("Mean: ", me)




from Package import median

medianodd = median.medianEven(1,3,2,3,4)
print("Median of Odd: ", medianodd)

medianeven = median.medianEven(1,2,3,4,5,6)
print("Median of Even: ", medianeven)