import logging

logger = logging.getLogger(__name__)


def _convert_spin(spin_text):
    """
    Change all the "{}" by "()" and change all "|" by a "+"

    Example:
      * spin : {{A|B}|{C|D}{E|F}}
      * spin converted : ((+)+(+)(+))
      * which will transform into a real operation in the method below
    """
    spin_converted = []
    for i in range(len(spin_text)):
        if spin_text[i] == '|':
            spin_converted.append("+")
        if spin_text[i] == '{':
            spin_converted.append("(")
        if spin_text[i] == '}':
            spin_converted.append(")")
    return spin_converted


def calculate_possibilities(spin_text):
    """
    Calculate the number of possibility in a Spin.

    Calls _convert_spin to put our spin in a mathematical operation format.
    Then we'll process the operation for the result.

    Example:
      * spin : {{A|B}|{C|D}{E|F|G}}
      * spin converted : ((+)+(+)(++))
      * spin converted after our treatment : ((2)+(2)*(3))
      * result = 8
    """
    operation = []
    spin_converted = _convert_spin(spin_text)
    local_sum = 1
    for i in range(len(spin_converted)):

        if spin_converted[i] == '+':
            # We want to calculate the numbers of variation inside a bracket
            # But if the sign "+" came after the end of a bracket, we just want to have the symbol "+"
            if spin_converted[i - 1] != ')':
                local_sum += 1
            if spin_converted[i - 1] == ')':
                operation.append("+")

        if spin_converted[i] == '(':
            if spin_converted[i - 1] == '+' and spin_converted[i - 2] != ')':
                # When we start a new bracket but we weren't in a bracket beforehand,
                # we need to get the current local sum before passing to the new bracket
                # we subtract 1 to the local sum because by default,
                # it will consider the new bracket as possibility
                # and because we'll add the new sum after we need to subtract it
                # Example :
                #       {A|B|{C|D}} has 1+1+(2) possibility
                #       it will be shown as (2+(2))
                #       and without the subtraction
                #       it would be 1+1+1+(2) so 3+(2) which is wrong
                operation.append(str(local_sum - 1))
                operation.append('+')
            if spin_converted[i - 1] == ')' and i != 0:
                # by default, eval don't multiply when two bracket is attach "(5)(4)" don't work
                # so we need to add a "*" between the two bracket so it will be (5)*(4) which work
                operation.append("*")

            operation.append('(')
            # We reinitialise the local value to sum how many possibility is inside this bracket
            local_sum = 1

        if spin_converted[i] == ')':
            # in the end of a bracket, we want to get the sum of the bracket
            # so we have only the sum of the bracket inside the bracket
            # But we don't want to get the sum inside two bracket's closure
            # then we close the bracket and reinitialise the local sum
            # Example:
            #       spin : {{A|B}|{C|Ð}}
            #       become ((2)+(2))
            #       instead of ((2)+(2)2) which is not what we want
            if spin_converted[i - 1] != ')':
                operation.append(str(local_sum))
            operation.append(")")
            local_sum = 1

        # Debug
        # to see every step of the processing
        # logger.debug(''.join(operation))

    result = eval(''.join(operation))
    logger.debug(''.join(operation))
    logger.debug(result)
    return result
