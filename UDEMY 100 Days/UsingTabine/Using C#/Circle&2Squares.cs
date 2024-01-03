private static int[] squareArray(int[] array)
{
    int[] result = new int[array.Length];
    for (int i = 0; i < array.Length; i++)
    {
        result[i] = (int)Math.Pow(array[i], 2);
    }
    return result;
}

squareArray(15[], 10)public static int CircleToSquareDifference(int radius)
{
    int square1 = (int)Math.Pow(radius, 2);
    int square2 = (int)Math.Floor(radius * Math.Sqrt(2));

    return square1 - square2;
}


public static int CircleToSquareDifference(int radius)
{
    int square1 = (int)Math.Pow(radius, 2);
    int square2 = (int)Math.Floor(radius * Math.Sqrt(2));

    return square1 - square2;
}

print(CircleToSquareDifference(5))