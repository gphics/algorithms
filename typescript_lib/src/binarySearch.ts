
/**
 * This function perfoms the binary search algorithm
 * @param arr : An array containing a list of numbers and it is expected to be a sorted array if not the function automatically sort it
 * @param target : A number to be searched for in the array
 * @returns : This function returns the index of the target in the sorted array or null if the target does not exist
 */
 function binarySearch(arr: number[], target: number): number | null {

    const sorted_arr = arr.sort((a: number, b: number) => a - b)

    let high: number = sorted_arr.length - 1
    let low: number = 0

    while (low <= high) {
        const mid: number = Math.floor((low + high) / 2)
        const guess: any = sorted_arr[mid]

        if (guess === target) {
            return mid
        } else if (guess < target) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }


    return null
}

export default binarySearch