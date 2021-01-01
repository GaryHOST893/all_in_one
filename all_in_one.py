# -*- coding: utf-8 -*-



print('\n')

print("Yo Baws, what you wana do?: ")

print("\n")

print("1. Performe an Internet Speed Test")

print("2. MetaHash Calculation")

print("3. Search WikiPedia")

print("4. Trade Calculation")

print("\n")



while True:



    choice = input("Yo Baws, what's it gonna be 1, 2, 3 or 4?: ")



    if choice == '1':



        import speedtest



        st = speedtest.Speedtest()

        

        print("Your download speed is" ,st.download()//10**6, "Mbps")

        print("Your upload speed is" ,st.upload()//10**6, "Mbps")

        print("Your ping is" ,int(st.results.ping), "Ms")



    elif choice == '2':



        # Choice to make simple MHC Transsaction calculations



        # Defining a Function which makes a simple addition when you buy a round number of MHC

        def bought_mhc(mhc_owned, mhc_bought):

            return mhc_owned + mhc_bought



        # Defining a Function which divides the amount of money spent with the price per MHC

        # in order to find out the exact number of MHC bought and adds it to number of MHC

        # already owned.

        def money_spent_to_buy_mhc(mhc_owned, sum_of_money_to_be_spend, mhc_buy_price):

            return mhc_owned + (sum_of_money_to_be_spend / mhc_buy_price)



        # Defining a Function which makes a simple subtraction when you sell a round number of MHC

        def sold_mhc(mhc_owned, mhc_sold):

            return mhc_owned - mhc_sold



        # Defining a Function which divides the amount of money desired to be made with the 

        # price per MHC in order to find out the exact number of MHC to be sold and subtracts

        # it to number of MHC already owned.

        def mhc_to_be_sold(mhc_owned, sum_of_money_to_be_made, mhc_sell_price):

            return mhc_owned - (sum_of_money_to_be_made / mhc_sell_price)



        # Trade Transaction Calculation

        def trade_mhc(mhc_owned, mhc_sell_price, mhc_buy_price, how_many_times_is_the_trade_to_be_repeated):

            return mhc_owned * ((mhc_sell_price / mhc_buy_price) ** how_many_times_is_the_trade_to_be_repeated)



        # Defining a Function which calculates the amount of money spent from this transaction

        def bought_transaction_value(mhc_to_be_bought, mhc_buy_price):

            return mhc_to_be_bought * mhc_buy_price



        # Defining a Function which calculates the amount of money spent from this transaction

        def sold_transaction_value(money_to_be_made, mhc_sell_price):

            return money_to_be_made / mhc_sell_price



        # Defining a Function which calculates the Node Payout

        def node_payout(mhc_owned, node_roi, node_percentage_payout):

            return mhc_owned * node_roi * node_percentage_payout / 100000



        num1 = float(input("Yo Baws, how many MHC do you own?: "))



        print("Yo Baws what you wanna do now?")

        print("1. Buy/Sell Transation Calculation")

        print("2. Trade Transaction Calculation")

        print("3. Node Payout Calculation")

        

        while True:



            # Take input from the user

            choice = input("Choice 1, 2 or 3 Baws?: ")



            # Choice 1 is to calculate buy transactions

            if choice == '1':



                num2 = float(input("Yo Baws, what's the trading price per MHC?: £/$/€ "))



                print("Yo Baws, are you looking to Buy or Sell?")

                print("1. Buy")

                print("2. Sell")



                while True:



                    choice = input("Choice 1 or 2 Baws?: ")

                

                    if choice == '1':



                        print("Yo Baws, do you know how many MHC you are looking to buy?")

                        print("1. Yes")

                        print("2. No")



                        while True:



                            choice = input("Choice 1 or 2 Baws?: ")



                            # Check if choice is one of two options

                            # Choice 1 is if you know how many MHC you want to buy

                            if choice == '1':



                                num3 = float(input("Yo Baws, how many MHC you wish to buy?: "))



                                print("Yo Baws, after this transaction you will have spent (", num3, "*", num2, "= ) £/$/€", bought_transaction_value(num3, num2))

                                print("Yo Baws, after this transaction you will own (", num1, "+", num2, "= )", bought_mhc(num1, num3), "MHC")

                            

                            # Choice 2 is if you do not know how many MHC you want to buy but you do know how much you want to spend

                            elif choice == '2':



                                num3 = float(input("Yo Baws, how much you spent?: £/$/€ "))



                                print("Yo Baws, after this transaction you will have bought (", num3, "/", num2, "= )", bought_transaction_value(num1, num2), "MHC")

                                print("Yo Baws, after this transaction you will own (", num1, "+", num3, "/", num2, "=", ")", money_spent_to_buy_mhc(num1, num3, num2), "MHC")

                    

                            break

                

                    # Choice 2 is to calculate sale transactions

                    elif choice == '2':



                        print("Yo Baws, do you know how many MHC you want to sell?: ")

                        print("1. Yes")

                        print("2. No")



                        while True:



                            choice = input("Choice 1 or 2 Baws?: ")



                            # Check if choise is one of two options

                            # Choice 1 is if you know how many MHC you want to sell

                            if choice == "1":

                                

                                num3 = float(input("Yo Baws, how many MHC you wish to sell?: "))

                                

                                print("Yo Baws, after this transaction you will have cashed-in (", num3, "*", num2, "= ) £/$/€", bought_transaction_value(num3, num2))

                                print("Yo Baws, after this transaction you will own (", num1, "-", num3, "= )", sold_mhc(num1, num3))



                            # Choice 2 is if you do not know how many MHC you want to sale but you know how much you want to cash-in

                            elif choice == "2":



                                num3 = float(input("Yo Baws, what sum of fiat you want to cash-in: £/$/€ "))



                                while True:

                                    

                                    # This is to check if the amount of MHC you currrently have is enough to afford the transaction

                                    if sold_mhc(num1, sold_transaction_value(num3, num2)) >= 0: 

                                        print("Yo Baws, after this transaction you will have sold (", num3, "/", num2, "= )", sold_transaction_value(num3, num2), "MHC")

                                        print("Yo Baws, after this transaction you will own (", num1, "-", sold_transaction_value(num3, num2), "= )", sold_mhc(num1, sold_transaction_value(num3, num2)), "MHC")

                                    

                                    else:

                                        print("Yooooo Baws...Your broke arse does not own enough MHC to afford this transaction")

                                

                                    break

                            break

                    break



                    # Choice 3 is calculate trading profit or loss

            elif choice == '2':



                num2 = float(input("Yo Baws, what price is MHC being sold at?: "))

                num3 = float(input("Yo Baws, what price is MHC being bought at?: "))

                num4 = float(input("Yo Baws, how many times you wanna execute the trade?: "))

                print( "Yo Baws, after these trades you will end up with (", num1, '*', "[(",num2, '/', num3, ") ^", num4,"] = ", trade_mhc(num1, num2, num3, num4), "MHC")



            elif choice == '3':



                num2 = float(input("Yo Baws, what is the ROI of the node?: "))

                num3 = float(input("Yo Baws, what is the payout %?: "))



                print("Yo Baws, if you invest on this Node you will get (", num1, "*", num2, "*", num3, "* 100 ) =", node_payout(num1, num2,num3), "MHC")



            break



    elif choice == '3':



        import wikipedia



        def search_wikipedia(question):

            answer = wikipedia.summary(question).split(".")

            for line in answer:

                print(line)



        if __name__ == "__main__":

            question = input("Yo Baws, what question you want to ask WikiPedia?: ")

            search_wikipedia(question)



    elif choice == '4':



        def risk_calculation(capital, risk_percentage):

            return capital * risk_percentage / 100

        

        def long_short_calculation(a, b, c):

            return (a / ( b - c ))



        def stop_loss_pip_calulation(trading_price, stop_loss_price, number_of_decimals):

            return ( trading_price - stop_loss_price) * 10 ** number_of_decimals



        def take_profit_pip_calulation(take_profit_price, trading_price, number_of_decimals):

            return ( take_profit_price - trading_price) * 10 ** number_of_decimals



        def potential_profit_or_loss(risk_calculation, b, c):

            return (risk_calculation - b) * c

        

        print("\n")

        num1 = float(input("Yo Baws, how much money does your broke arse has to invest?: "))

        num2 = float(input("and what percentage is your broke arse confy risking?: "))

        num3 = str(input("and what pair are you thinking to invest im Baws?: "))

        num4 = float(input("and how many decimals per point Baws?: "))

        num5 = float(input("and at what price is the pair trading at Baws?: "))

        print("\n")



        print("Yo Baws, what you gonna do?: ")

        print("\n")

        print("1. Go Long")

        print("2. Go Short")

        print("\n")



        while True:



            choice = input("Yo Baws, what's it gonna be 1 or 2?: ")

                

            if choice == '1':

                

                print("\n")

                num6 = float(input("Yo Baws, what's the Stop Loss?: "))

                num7 = float(input("and what about Take Profit?: "))

                print("\n")



                print("So Baws, this are the Trade Transaction brake down information:")

                print("\n")

                print("Starting Capital: ", num1, " £/$/€")

                print("Investment Pair: ", num3)

                print("Capital Risk: ", risk_calculation(num1, num5), " £/$/€")

                print("Stop Loss: ", num6, " £/$/€")

                print("Stop Loss PiP: ", stop_loss_pip_calulation(num5, num6, num2))

                print("Potential Loss ", potential_profit_or_loss(num5, num6 , long_short_calculation(risk_calculation(num1, num2), num5, num6)), " £/$/€")

                print("Take Profit: ", num7, " £/$/€")

                print("Potential Profit: ", potential_profit_or_loss(num7, num5, long_short_calculation(risk_calculation(num1, num2, num5, num6)), " £/$/€")

                print("PiP Profit: ", take_profit_pip_calulation(num7, num5, num4))

                

            

            elif choice == '2':

                

                print("\n")

                num5 = float(input("Yo Baws, what's the Stop Loss?: "))

                num6 = float(input("and what about Take Profit?: "))

                print("\n")



                print("So Baws, this are the Trade Transaction brake down information:")

                print("\n")

                print("Starting Capital: ", num1, " £/$/€")

                print("Investment Pair: ", num2)

                print("Capital Risk: ", risk_calculation(num1, num5), " £/$/€")

                print("Stop Loss: ", num6, " £/$/€")

                print("Stop Loss PiP: ", stop_loss_pip_calulation(num5, num6, num3))

                print("Potential Loss ", potential_profit_or_loss(num5, num6 , long_short_calculation(risk_calculation(num1, num4), num5, num6)), " £/$/€")

                print("Take Profit: ", num7, " £/$/€")

                print("Potential Profit: ", potential_profit_or_loss(num7, num5, long_short_calculation(risk_calculation(num1, num4), num5, num6)), " £/$/€")

                print("PiP Profit: ", take_profit_pip_calulation(num7, num5, num3))

                print("Investment per Point: ", long_short_calculation(risk_calculation(num1, num4), num5, num6), " £/$/€")

            



            break

            

    else:



        print("Yo Baws, yo arse is dumb as FUCK !!! Follow the fucking INSTRUCTIONS properly Bruh!!!")

    

    break