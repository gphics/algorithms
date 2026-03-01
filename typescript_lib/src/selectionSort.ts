
/**
 * 
 * @param arr : an unsorted array
 * @returns : the index of the smallest element
 */
function findSmallest(arr: number[]): number{
    
    // setting default values
    let smallest = arr[0] as number
    let smallestIndex = 0

    // looping through the arr starting from the second element
    for (let i = 1; i < arr.length; i++){
        const currentElem = arr[i] as number
        if (currentElem < smallest) {
            smallest = currentElem
            smallestIndex = i
        }
    }

    // returning the 
    return smallestIndex 
}

/**
 * 
 * @param arr : an unsorted array containing numbers
 * @returns : a sorted array
 */
export default function selectionSort(arr: number[]): number[] {
    
    const copiedArr = [...arr]
    const sortedArr: number[] = []
    const initialLength = copiedArr.length
    
    // looping
    for (let i = 0; i < initialLength ; i++){
        const smallestIndex: number = findSmallest(copiedArr)
        const smallest: number = copiedArr.splice(smallestIndex, 1)[0] as number
        sortedArr.push(smallest)
    }


    return sortedArr
    
}

