#!/usr/bin/env python

import random

class my_stat():
    def __init__(calc, days):
        calc.days = days + 1
        calc.allValues = []
        calc.totalValues = []
        calc.weird = []
        calc.g = None
        calc.r = None
        calc.s = None
        calc.alrt_sw = []
        calc.index_sw = 0
        calc.nbr_sw = 0
        calc.key_sw = 0

    def myinput(calc):
        try:
            value = input()
            value = float(value)
        except ValueError:
            if value == "STOP":
                return value
            else:
                exit (84)
        except KeyboardInterrupt:
            exit(84)
        except EOFError:
            exit(84)
        return value

    def moyenneG(calc, d_period):
        if (calc.days != 0):
            return
        i = d_period
        x = 0
        calc.g = 0
        while (i != 0):
            if (calc.allValues[x + 1] > calc.allValues[x]):
                res = calc.allValues[x + 1] - calc.allValues[x]
                calc.g = calc.g + res
            x += 1
            i -= 1
        calc.allValues.pop(0)
        calc.g = calc.g / d_period
        calc.g = "%.2f" % round(calc.g, 2)


    def difR(calc, d_period):
        if (calc.days != 0):
            return
        calc.r = 0
        res = calc.allValues[d_period] - calc.allValues[0]
        calc.r = res / calc.allValues[0]
        calc.r = calc.r * 100
        calc.r = round(calc.r)
        calc.alrt_sw.append(calc.r)
        calc.index_sw = calc.index_sw + 1

    def deviationS(calc, d_period):
        if (calc.days > 1):
            return
        i = d_period
        x = 0
        calc.s = 0
        moyenne = 0
        while (i != 0):
            res = calc.allValues[x]
            moyenne = moyenne + res
            x += 1
            i -= 1
        moyenne = moyenne / d_period
        j = d_period
        while (j != 0):
            tmp = calc.allValues[i] - moyenne
            tmp = tmp * tmp
            calc.s = calc.s + tmp
            i += 1
            j -= 1
        calc.s = calc.s / d_period
        calc.s = pow(calc.s, 0.5)
        calc.s = "%.2f" % round(calc.s, 2)

    def weirdestValue(calc):
        i = 5
        x = 0
        while (i != 0):
            calc.weird.append(random.choice(calc.totalValues))
            i -= 1
            x += 1

    def alerteSwitch(calc):
        if (calc.days != 0):
            return
        if (calc.index_sw > 1):
            if (calc.alrt_sw[calc.index_sw - 2] > 0 and calc.alrt_sw[calc.index_sw - 1] < 0):
                calc.nbr_sw = calc.nbr_sw + 1
                calc.key_sw = 1
            elif (calc.alrt_sw[calc.index_sw - 2] < 0 and calc.alrt_sw[calc.index_sw - 1] > 0):
                calc.nbr_sw = calc.nbr_sw + 1
                calc.key_sw = 1
            else:
                return

    def resultPrint(calc):
            if (calc.days > 0):
                if (calc.days == 1):
                   print("g=nan\t\tr=nan%\t\ts=" + str(calc.s))
                else:
                    print("g=nan\t\tr=nan%\t\ts=nan")
            elif (calc.key_sw == 0):
                print("g=" + str(calc.g) + "\t\tr=" + str(calc.r) + "%\t\ts=" + str(calc.s))
            else:
                print("g=" + str(calc.g) + "\t\tr=" + str(calc.r) + "%\t\ts=" + str(calc.s) + "\t\ta switch occurs")
                calc.key_sw = 0


    def loop(calc):
        d_period = calc.days - 1
        while True:
            value = calc.myinput()
            if (value == "STOP"):
                try:
                    calc.weirdestValue()
                    print("Global tendency switched " + str(calc.nbr_sw) + " times")
                    print("5 weirdest values are " + str(calc.weird))
                    return False
                except:
                    exit (84)
            else:
                calc.allValues.append(value)
                calc.totalValues.append(value)
                if (calc.days > 0):
                    calc.days = calc.days - 1
                calc.difR(d_period)
                calc.moyenneG(d_period)
                calc.deviationS(d_period)
                calc.alerteSwitch()
                calc.resultPrint()

