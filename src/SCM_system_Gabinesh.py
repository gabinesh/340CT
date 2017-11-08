import tkinter as tk
from tkinter import *
import login #login process initializing
import refund #refund process initializing
import viewSales #viewSales process initializing
import delete #delete process initializing

class main(tk.Tk):
    """Main class template that stores the master details for all pages and stores pages into
        dictionary to move between menus and functionalities
        """
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) 

        #main frame template below
        Main = tk.Frame(self)
        Main.pack(side="top", expand = False)
        Main.grid_rowconfigure(0, weight=1)
        Main.grid_columnconfigure(0, weight=1)

        
        self.pages = {} #all pages are stored inside a dictionary

        
        #storing pages into dictionary
        #first_page = login_page(Main, self)
        #second_page = refund_page(Main, self)
        third_page = view_sales_trend_delete(Main, self)
        #fourth_page = menu(Main,self)
        
        #self.pages[login_page] = first_page
        #self.pages[refund_page] = second_page
        self.pages[view_sales_trend_delete] = third_page
        #self.pages[menu] = fourth_page
        
        #first_page.grid(sticky="nsew")
        #second_page.grid(sticky="nsew")
        third_page.grid(sticky="nsew")
        #fourth_page.grid(sticky="nsew")
        

        self.open_window(login_page)#runs the first page i.e. login page


        
    def open_window(self, window):
        """Function that switches the showing of pages
            i.e main menu to refund page etc"""
        open_window1 = self.pages[window]
        open_window1.tkraise()



            
class menu(tk.Frame):
      """Main menu class that holds the buttons which switches between functionalities"""
      def __init__(self, parent, process):
        tk.Frame.__init__(self, parent)

        #setting background for main menu
        self.background1 = tk.PhotoImage(file='menu.png')
        wallpaper1 = tk.Label(self,image=self.background1)
        wallpaper1.grid()

        #refund functionality button which switches from menu to refund page
        Refund = tk.Button(self,text="Refund",font="Helvetica 20 bold",command=lambda:process.open_window(refund_page))
        Refund.place(x=795, y=505)
        
        #refund functionality button which switches from menu to view_sales_trend_delete page
        view_stock = tk.Button(self, font="Helvetica 20 bold",text="View Stock/delete",command=lambda:process.open_window(view_sales_trend_delete))
        view_stock.place(x=735, y=605)

        
            
class refund_page(tk.Frame):
    
    """refund class GUI that holds the buttons and messages which communicate between refund processor orderly
       and generates notification boxs/display windows to match the broker diagram"""
    
    def __init__(self, parent, process):
        tk.Frame.__init__(self, parent)

        #setting background for refund page
        self.background1 = tk.PhotoImage(file='refund.png')
        wallpaper1 = tk.Label(self,image=self.background1)
        wallpaper1.grid()

        #Button to go back home
        go_Back = tk.Button(self,font="Helvetica 20 bold", text="Back To Menu",command=lambda:process.open_window(menu))
        go_Back.place(x=1600, y=20)


        #we create the insert item code title box and disables the title box 
        item_code_text = StringVar()
        item_code_text.set("Item Code")
        item_code_title = tk.Entry(self, width=20,font=("Helvetica", 12, "bold"),textvariable=item_code_text)
        item_code_title.place(x=45, y=500)
        item_code_title.config(state='disabled')

        #we create the insert item code entry box 
        self.item_code = tk.Entry(self, width=20,font=("Helvetica", 12, "bold") )
        self.item_code.place(x=205, y=500)

        #if item code is being used as the method of input than we disable item name entry to limit confusion/errors and show item code entry as selected
        self.use_code = tk.Button(self,text="Selected",font="Helvetica 10 bold",command=lambda:select_code())
        self.use_code.place(x=385, y=500)
        self.use_code.config(state='disabled')

        #we create the insert item name title box and disables the title box 
        item_name_text = StringVar()
        item_name_text.set("Item Name")
        item_name_title = tk.Entry(self, width=20,font=("Helvetica", 12, "bold"),textvariable=item_name_text)
        item_name_title.place(x=45, y=600)
        item_name_title.config(state='disabled')

        #if item NAME is being used as the method of input than we disable item code entry to limit confusion/errors and show item name entry as selected
        self.item_name = tk.Entry(self, width=20,font=("Helvetica", 12, "bold"))
        self.item_name.place(x=205, y=600)
        self.item_name.config(state='disabled')
        self.use_name = tk.Button(self,text="Select",font="Helvetica 10 bold",command=lambda:select_name())
        self.use_name.place(x=385, y=600)
        
        #we create the insert item price title box and disables the title box 
        item_price_text = StringVar()
        item_price_text.set("Item Price")
        item_price_title = tk.Entry(self, width=20,font=("Helvetica", 12, "bold"),textvariable=item_price_text)
        item_price_title.place(x=45, y=700)
        item_price_title.config(state='disabled')

        #we create the insert item price title box and disables the title box 
        self.item_price = tk.Entry(self, width=20,font=("Helvetica", 12, "bold"))
        self.item_price.place(x=205, y=700)

        #we create the refund Description title box and disable the title box 
        refund_description_text = StringVar()
        refund_description_text.set("Refund Description")
        refund_description_title = tk.Entry(self, width=50,font=("Helvetica", 12, "bold"),textvariable=refund_description_text)
        refund_description_title.place(x=705, y=478)
        refund_description_title.config(state='disabled')

        #we create the insert refund reason/discription window for user input
        self.refund_description = tk.Text(self, width=50,height=12,font=("Helvetica", 12, "bold"))
        self.refund_description.place(x=705, y=500)
        

        #we create the complete button to lock the refund description after its been written in
        self.complete_button = tk.Button(self,text="Complete",font="Helvetica 10 bold",command=lambda:complete())
        self.complete_button.place(x=1087, y=735)

        #we create the complete button to begin the refund procedure notification before updateing our returned items table i.e. are you sure you want to refund?
        self.confirm_button = tk.Button(self,text="Confirm Refund",font="Helvetica 10 bold",command=lambda:confirm())
        self.confirm_button.place(x=855, y=805)
        self.confirm_button.config(state='disabled')

        
        
        def complete():
            """Function to disable refund description window once it has been filled in and enable the confirm button
                to prepare the user to proceed to the refunding of the item and storing the refun into the returned table"""
            self.complete_button.destroy()
            self.incomplete_button = tk.Button(self,text="Incomplete",font="Helvetica 10 bold",command=lambda:incomplete())
            self.incomplete_button.place(x=1078, y=735)
            self.refund_description.config(state='disabled')
            self.confirm_button.config(state='normal')

            
        def incomplete():
            """Function that disables the confirm button if the user decides they are unsure about the refund discription/refunding the
               item acts as pre-cancel"""
            self.incomplete_button.destroy()
            self.complete_button = tk.Button(self,text="Complete",font="Helvetica 10 bold",command=lambda:complete())
            self.complete_button.place(x=1087, y=735)
            self.refund_description.config(state='normal')
            self.confirm_button.config(state='disabled')

        self.code_selected = 1 # since using item code is selected on startup we give prepare refund proccessor to use code and not name
        self.name_selected = 0
 
        def select_name():
            """Function to disable the select button once the user selects use name and changes the use name select button to selected"""
            self.code_selected = 0
            self.name_selected = 1 #prepare refund proccessor to use name and not code
            
            self.use_code.destroy()
            self.use_name.destroy()
            self.item_name.config(state='normal')
            self.item_code.config(state='disabled')
            self.use_code = tk.Button(self,text="Select",font="Helvetica 10 bold",command=lambda:select_code())
            self.use_code.place(x=385, y=500)
            self.use_code.config(state='normal')
            self.use_name = tk.Button(self,text="Selected",font="Helvetica 10 bold")
            self.use_name.place(x=385, y=600)
            self.use_name.config(state='disabled')

                
        def select_code():
            """Function to disable the select button once the user selects use code and changes the use code select button to selected"""
            
            self.code_selected = 1#prepare refund proccessor to use code and not name
            self.name_selected = 0
     
            self.use_code.destroy()
            self.use_name.destroy()
            self.item_name.config(state='disabled')
            self.item_code.config(state='normal')
            self.use_code = tk.Button(self,text="Selected",font="Helvetica 10 bold")
            self.use_code.place(x=385, y=500)
            self.use_code.config(state='disabled')
            self.use_name = tk.Button(self,text="Select",font="Helvetica 10 bold",command=lambda:select_name())
            self.use_name.place(x=385, y=600)
            self.use_name.config(state='normal')


        

                
            
        def confirm():
            """Function that sends all the details inputted to the refund processor to carry out the refunding of the item"""
            
            def cancel():
                """cancel function(for cancel button) to destroy all buttons that proceed to refund processor"""
                self.ok_button.destroy()
                self.cancel_button.destroy()
                self.confirmation.destroy()
                
                    
            def close():
                """close function(for close button) to destroy final refund notification and destroys all other pre notifications"""
                self.confirmation2.destroy()
                self.close_button.destroy()
                self.incomplete_button.destroy()
                self.confirm_button.config(state='disabled')
                self.complete_button = tk.Button(self,text="Complete",font="Helvetica 10 bold",command=lambda:complete())
                self.complete_button.place(x=1087, y=735)
                self.refund_description.config(state='normal')
            
            if self.code_selected == 1:

                """if use code is selected than refund item according to the code inputted"""
                
                will = refund.refundItem(self.item_code.get(),"code")#sends details to refund processor to return item details that will be refunded

                #generates the confirmation code before refunding item so that user knows what will be refunded(not refunded yet)
                text1 = "you wish to return item " + str(will[1]) + ". You are returning to the customer "+"\n"+" an amount of £"\
                       + str(self.item_price.get())+ ". The current quantity is " +str(will[3]) + " and after the return "\
                       "it will be "+ str(int(will[3]+1)) + "\n"+". The price is £" + str(will[2]) + ". Make sure your returning the correct amount."
                self.confirmation = tk.Label(self, width=59,height=3,font=("Helvetica", 7, "bold"),text=text1)
                self.confirmation.place(x=705, y=737)
                self.confirmation.config(state='disabled')

                #creates the ok and cancel button once user finishes inputing all details
                self.ok_button = tk.Button(self,width=7,text="OK",font="Helvetica 10 bold",command=lambda:ok())
                self.ok_button.place(x=855, y=805)
                self.cancel_button = tk.Button(self,text="Cancel",font="Helvetica 10 bold",command=lambda:cancel())
                self.cancel_button.place(x=920, y=805)
                
                
                def ok():
                    """OK function that sends the details to refund processor and refunds the item according to the item code"""
                    self.ok_button.destroy()
                    self.cancel_button.destroy()
                    self.confirmation.destroy()
                    listForReturnAndRefund = [will[1],self.item_price.get(),self.refund_description.get('1.0', END)]
                    text2 = refund.ReturnAndRefund(listForReturnAndRefund)
                    self.confirmation2 = tk.Label(self, width=60,height=20,font=("Helvetica", 17, "bold"),text=text2)
                    self.confirmation2.place(x=555, y=357)
                    self.confirmation2.config(state='disabled')
                    self.close_button = tk.Button(self,width=7,text="Close",font="Helvetica 10 bold",command=lambda:close())
                    self.close_button.place(x=965, y=865)

                
                    
            if self.name_selected == 1:
                
                """if use name is selected than refund item according to the name inputted"""
                
                will = refund.refundItem(self.item_name.get(),"name")#sends details to refund processor to return item details that will be refunded

                #generates the confirmation code before refunding item so that user knows what will be refunded(not refunded yet)
                text2 = "you wish to return item " + str(will[1]) + ". You are returning to the customer "+"\n"+" an amount of £"\
                       + str(self.item_price.get())+ ". The current quantity is " +str(will[3]) + " and after the return "\
                       "it will be "+ str(int(will[3]+1)) + "\n"+". The price is £" + str(will[2]) + ". Make sure your returning the correct amount."
                self.confirmation = tk.Label(self, width=59,height=3,font=("Helvetica", 7, "bold"),text=text1)
                self.confirmation.place(x=705, y=737)
                self.confirmation.config(state='disabled')
                
                #creates the ok and cancel button once user finishes inputing all details
                self.ok_button = tk.Button(self,width=7,text="OK",font="Helvetica 10 bold",command=lambda:ok())
                self.ok_button.place(x=855, y=805)
                self.cancel_button = tk.Button(self,text="Cancel",font="Helvetica 10 bold",command=lambda:cancel())
                self.cancel_button.place(x=920, y=805)
                
                def ok():
                    """OK function that sends the details to refund processor and refunds the item according to the item code"""
                    self.ok_button.destroy()
                    self.cancel_button.destroy()
                    self.confirmation.destroy()
                    listForReturnAndRefund = [will[1],self.item_price.get(),self.refund_description.get('1.0', END)]
                    text2 = refund.ReturnAndRefund(listForReturnAndRefund)
                    self.confirmation2 = tk.Label(self, width=120,height=45,font=("Helvetica", 7, "bold"),text=text2)
                    self.confirmation2.place(x=555, y=357)
                    self.confirmation2.config(state='disabled')
                    self.close_button = tk.Button(self,width=7,text="Close",font="Helvetica 10 bold",command=lambda:close())
                    self.close_button.place(x=895, y=805)

                

        

class view_sales_trend_delete(tk.Frame):
    def __init__(self, parent, process):
        tk.Frame.__init__(self, parent)
        
        """view_sales_trend_delete class GUI that holds the buttons and messages which communicate between viewSales/delete processors orderly
       and generates notification boxs/display windows to match the broker diagram"""

        #sets background for frame
        self.background = tk.PhotoImage(file='sales.png')
        wallpaper = tk.Label(self,image=self.background)
        wallpaper.grid()

        #creates go back to menu button
        go_Back = tk.Button(self,font="Helvetica 20 bold", text="Back To Menu",command=lambda:process.open_window(menu))
        go_Back.place(x=1600, y=60)

        #creates delete button 
        self.delete_button = tk.Button(self,width=12,text="Delete item",font="Helvetica 15 bold",command=lambda:deleteItem())
        self.delete_button.place(x=1090, y=415)
            
        
        def updateStockWindow():
            """generates the Text box which will display the stock table with daily sales trend"""
            sales_trend_Titles = "Code          |                      Name                        |   Quantity  |  Trend" #column titles
            self.sales_trend_LABEL = tk.Text(self, width=61,height=1,font="Helvetica 15 bold")
            self.sales_trend_LABEL.insert('1.0', sales_trend_Titles)
            self.sales_trend_LABEL.place(x=200, y=170) 
            self.sales_trend_LABEL.configure(state="disabled")

            #create text boxes for each column to display each item in stock in individual boxes where each item is on a seperate line but the
            #values remain on the same line
            self.sales_trend_CODE = tk.Text(self, width=10,height=30,font="Helvetica 15 bold")
            self.sales_trend_CODE.place(x=200, y=200)
            self.sales_trend_NAME = tk.Text(self, width=30,height=30,font="Helvetica 15 bold")
            self.sales_trend_NAME.place(x=315, y=200)
            self.sales_trend_QUANTITY = tk.Text(self, width=10,height=30,font="Helvetica 15 bold")
            self.sales_trend_QUANTITY.place(x=650, y=200)
            self.sales_trend_TREND = tk.Text(self, width=10,height=30,font="Helvetica 15 bold")
            self.sales_trend_TREND.place(x=765, y=200)

            #communicates with the viewSales/stock processor to get the information for all items stored in the database
            listAllDetails = viewSales.loadStock()#viewSales/stock processor returns multiple lists each list contains all values or one column

            #extracting each list which contain single column values
            code = listAllDetails[0]
            name = listAllDetails[1]
            quantity = listAllDetails[2]
            trend = listAllDetails[3]

            
            for i in range (1,len(code)+1):
                #for loop which displacys values stored in each list to dislay items in the view stock window
                self.sales_trend_CODE.insert('1.0', str(code[-i]) +'\n')
                self.sales_trend_NAME.insert('1.0', name[-i]+'\n')
                self.sales_trend_QUANTITY.insert('1.0', str(quantity[-i])+'\n')
                self.sales_trend_TREND.insert('1.0', trend[-i]+'\n')
            
            #disabling each text box so that we can only view not edit view stock window
            self.sales_trend_CODE.configure(state="disabled")   
            self.sales_trend_NAME.configure(state="disabled")   
            self.sales_trend_QUANTITY.configure(state="disabled")
            self.sales_trend_TREND.configure(state="disabled")

            #create item entry box/title for user to input item code that they wish to delete from stock database accorind to its Trend in sales
            item_code_text = StringVar()
            item_code_text.set("          Item Code")
            item_code_title = tk.Entry(self, width=20,font=("Helvetica 12 bold"),textvariable=item_code_text)
            item_code_title.place(x=1075, y=365)
            item_code_title.config(state='disabled')
            self.item_code = tk.Entry(self, width=20,font=("Helvetica", 12, "bold") )
            self.item_code.place(x=1075, y=385)

            #assings delete button to send all details to delete processor to delete low selling items permanantly
            self.delete_button = tk.Button(self,width=12,text="Delete item",font="Helvetica 15 bold",command=lambda:deleteItem())
            self.delete_button.place(x=1090, y=415)
            
        updateStockWindow()

        
        def deleteItem():
            """function that sends details to delete processor to finilize and delete the item from all tables and
               returns final delete notification status"""
            
            def complete():
                """Once deleted destory final notification"""
                self.sales_trend_Notification.destroy()
                self.close_button1.destroy()
                
                
            def cancel():
                """function to cancel final deletion and does not forward details to delete processor"""
                self.sales_trend_Notification.destroy()
                self.ok_button.destroy()
                self.cancel_button.destroy()

            def Ok():
                """Function to confirm final deletion to the delete processor and recieves the notification text from the delete processer"""
                display = delete.prompt(self.item_code.get())#gets the delete notification details from the delete processor (for final notification string)
                deleteItem = delete.deleteItem(self.item_code.get())#sends details to delete processor to actually delete the item
                self.sales_trend_Notification.destroy()


                #string which holds the final delete message
                sales_trend_Titles = "You have successfully deleted"+'\n'*2+"item code:" + str(display[0]) + '\n' + "item name: " + display[1] + '\n'*2+"Stock table window has been update"

                #creates final notification box
                self.sales_trend_Notification = tk.Text(self, width=61,height=6,font="Helvetica 15 bold")
                self.sales_trend_Notification.insert('1.0', sales_trend_Titles)#displays final notification message in notification box
                self.sales_trend_Notification.place(x=1200, y=500) 
                self.sales_trend_Notification.configure(state="disabled")

                #deletes all previous ok/cancel buttons and clears the unmodified view stock/trends table
                self.ok_button.destroy()
                self.cancel_button.destroy()
                self.close_button1 = tk.Button(self,width=12,text="Close",font="Helvetica 12 bold",command=lambda:complete())
                self.close_button1.place(x=1480, y=650)
                self.sales_trend_LABEL.destroy()
                self.sales_trend_CODE.destroy()
                self.sales_trend_NAME.destroy()
                self.sales_trend_QUANTITY.destroy()
                self.sales_trend_TREND.destroy()

                #updates the new view stock/trends table with the deleted item finally deleted
                updateStockWindow()

            #creates the pre deletion notification message   
            display = delete.prompt(self.item_code.get())#gets the details from delete processor as a list
            sales_trend_Titles = "You wish to delete"+'\n'*2+"item code:" + str(display[0]) + '\n' + "item name: " + display[1] + '\n' + "Quantity: " +  str(display[2])
            self.sales_trend_Notification = tk.Text(self, width=61,height=6,font="Helvetica 15 bold")
            self.sales_trend_Notification.insert('1.0', sales_trend_Titles)
            self.sales_trend_Notification.place(x=1200, y=500) 
            self.sales_trend_Notification.configure(state="disabled")
            self.ok_button = tk.Button(self,width=12,text="OK",font="Helvetica 12 bold",command=lambda:Ok())#button  that confirms deletion
            self.ok_button.place(x=1400, y=650)
            self.cancel_button = tk.Button(self,width=12,text="CANCEL",font="Helvetica 12 bold",command=lambda:cancel())#button  that cancels deletion
            self.cancel_button.place(x=1550, y=650)

            
                                
class login_page(tk.Frame):
     """Login class GUI that holds the buttons and messages which communicate between login processor orderly
       and generates notification boxs/display windows to match the broker diagram"""
     def __init__(self, parent, process):
        tk.Frame.__init__(self, parent)
        self.background = tk.PhotoImage(file='login.png')

        #sets background for login page
        wallpaper = tk.Label(self,image=self.background)
        wallpaper.grid()

            
        username = tk.StringVar() #prepares username login entry details as an input
        username = tk.Entry(self, width=39,font=("Helvetica", 12, "bold"))
        username.place(x=725, y=800)
   
        password = tk.StringVar() #prepares password login entry details as an input
        password = tk.Entry(self, width=39,font=("Helvetica", 12, "bold"))
        password.place(x=725, y=830)

        #creates login button which runs the validation process for login
        login_button = tk.Button(self,text="Login", width=10,height=2,command = lambda:check())
        login_button.place(x=1085, y=805)            
    
        def check():
            """sends input details to login processor to see it runs through validation checks"""
            u = username.get()
            p = password.get()
            if login.login_check(u,p)== True:
                #if validation succesful than move to menu page
                process.open_window(menu)
       

run = main()
run.mainloop()
        


        



