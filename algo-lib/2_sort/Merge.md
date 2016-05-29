# bottom-up merge sort

    split each element into partitions of size 1
    recursively merge adjacent partitions
        for i = [leftPartStartIndex : rightPartLastIndex]
            if leftPartHeadValue <= rightPartHeadValue
                copy leftPartHeadValue
            else
                copy rightPartHeadValue
        copy elements back to original array


# top-down mergesort

    recursively sort array[loIndex : hiIndex]
        if loIndexVal >= HiIndexVal: return
        split array into 2 parts from midIndex
        sort leftPart of array
        sort rightPart of array
        merge array from 2 parts:
            if leftPartHeadValue <= rightPartHeadValue:
                copy leftPartHeadValue
            else:
                copy rightPartHeadValue
            copy element back to original array
