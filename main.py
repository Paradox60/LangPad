#pylint:disable=E0001
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.graphics import Color, Rectangle


from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.slider import Slider



from kivy.properties import StringProperty


from kivy.factory import Factory
from functools import partial


# from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import os
# --------------------------------------------------------------------

from BaseClass import Create_cursor
from Functions import *


# --------------------------------------------------------------------


class Main_Window(Screen):


    def prepare(self):
        os.remove('log.db')
        # Open Base and take number of word
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        Base_Est.Create_Table()
        Memory_log.Create_Memory_Table()
        Volume = Base_Est.Number_Of_Elements()
        Time = Now_Time()

        # Check word base and macking a list which has number of valid words
        Valid_words = []
        All_Words = []
        for count in range(0, Base_Est.Number_Of_Elements()):
            All_Words.append(count)
            # print(count)
            if Base_Est.Pick_Up_Single_Value(count, 3) == 100:
                if (Time - Base_Est.Pick_Up_Single_Value(count, 4)) >= 200000:
                    Base_Est.Update_progress_value(count + 1, 90)
                    Valid_words.append(count)
                else:
                    Base_Est.Update_progress_value(count + 1, 100)
            else:
                Valid_words.append(count)

        Base_Est.Print_Data()
        print(Valid_words)
        random.shuffle(Valid_words)
        print(Valid_words)
        print(All_Words)
        if len(Valid_words) == 0 or Base_Est.Number_Of_Elements() < 4:
            print('Слов мало')
            self.caution = Caution(self)
            self.caution.open()
            Base_Est.Close_Database()
            Memory_log.Close_Database()

        else:


            # Macking log base with words which be asked
            for i in range(0, 10):




                ran_que = Valid_words[i]
                ran_ans = Gen_Num(All_Words,ran_que)

                # Shuffle list
                answer_list = Shuffle(ran_que, ran_ans)

                log = {'Right_ans': ran_que, 'RB': answer_list[0], 'RT': answer_list[1], 'LB': answer_list[2],
                       'LT': answer_list[3], 'Ans': -1, 'Position': 0}
                Memory_log.Write_Genereted_Answer(log)
                #ran_que = random.choice(Valid_words)

                i += 1
                if i == len(Valid_words):
                    break

            Memory_log.Update_position_value(1, 1)
            Memory_log.Print_Data()
            print('______________________________________')
        self.manager.current = 'test'
        Base_Est.Close_Database()
        Memory_log.Close_Database()


class Testing(Screen):
    que_num = 1

    def on_pre_enter(self, *args):
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        self.ids.RT.disabled = False
        self.ids.RB.disabled = False
        self.ids.LT.disabled = False
        self.ids.LB.disabled = False

        LBL = Memory_log.Pick_Up_Single_Value(0, 1)
        RT = Memory_log.Pick_Up_Single_Value(0, 2)
        RB = Memory_log.Pick_Up_Single_Value(0, 3)
        LT = Memory_log.Pick_Up_Single_Value(0, 4)
        LB = Memory_log.Pick_Up_Single_Value(0, 5)

        self.que_num = 1
        self.ids.FORW.text = 'Forward'
        self.ids.QUE_WORD.text = Base_Est.Pick_Up_Single_Value(LBL , 1)
        self.ids.RT.text = Base_Est.Pick_Up_Single_Value(RT, 2)
        self.ids.RB.text = Base_Est.Pick_Up_Single_Value(RB, 2)
        self.ids.LT.text = Base_Est.Pick_Up_Single_Value(LT, 2)
        self.ids.LB.text = Base_Est.Pick_Up_Single_Value(LB, 2)
        self.ids.POS.text = 'Вопрос №'+str(self.que_num)

        # Memory_log.Update_progress_value(8, True)
        Base_Est.Close_Database()
        Memory_log.Close_Database()

    # ----------------------------------------------------------------------------

    def on_enter(self, *args):
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        self.ids.RT.disabled = False
        self.ids.RB.disabled = False
        self.ids.LT.disabled = False
        self.ids.LB.disabled = False

        LBL = Memory_log.Pick_Up_Single_Value(0, 1)
        RT = Memory_log.Pick_Up_Single_Value(0, 2)
        RB = Memory_log.Pick_Up_Single_Value(0, 3)
        LT = Memory_log.Pick_Up_Single_Value(0, 4)
        LB = Memory_log.Pick_Up_Single_Value(0, 5)

        self.ids.FORW.text = 'Forward'
        self.ids.QUE_WORD.text = Base_Est.Pick_Up_Single_Value(LBL, 1)
        self.ids.RT.text = Base_Est.Pick_Up_Single_Value(RT, 2)
        self.ids.RB.text = Base_Est.Pick_Up_Single_Value(RB, 2)
        self.ids.LT.text = Base_Est.Pick_Up_Single_Value(LT, 2)
        self.ids.LB.text = Base_Est.Pick_Up_Single_Value(LB, 2)

        Base_Est.Close_Database()
        Memory_log.Close_Database()

    # ----------------------------------------------------------------------------

    def answer_checking_RT(self):
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        for find in range(0, Memory_log.Number_Of_Elements()):
            if Memory_log.Pick_Up_Single_Value(find, 7) == '0':
                position = find - 1
                break
            elif find == Memory_log.Number_Of_Elements() - 1:
                position = Memory_log.Number_Of_Elements() - 1
                self.ids.QUE_WORD.text = 'Test is complite'
                Memory_log.Print_Data()





            else:
                find += 1
                # print('find', find)
        if Memory_log.Pick_Up_Single_Value(position, 6) == -1 and Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements()-1,6) == -1:

            LBL = Memory_log.Pick_Up_Single_Value(position, 1)
            RT = Memory_log.Pick_Up_Single_Value(position, 2)
            RB = Memory_log.Pick_Up_Single_Value(position, 3)
            LT = Memory_log.Pick_Up_Single_Value(position, 4)
            LB = Memory_log.Pick_Up_Single_Value(position, 5)

            if LBL == RT:
                self.ids.RT.background_color = (0, 1, 0, 0.8)
            else:
                self.ids.RT.background_color = (1, 0, 0, 0.8)

            if RB == LBL:
                self.ids.RB.background_color = (0, 1, 0, 0.8)
            else:
                if LT == LBL:
                    self.ids.LT.background_color = (0, 1, 0, 0.8)
                else:
                    if LB == LBL:
                        self.ids.LB.background_color = (0, 1, 0, 0.8)

            Memory_log.Update_ans_value(position + 1, Memory_log.Pick_Up_Single_Value(position, 2))

            Memory_log.Print_Data()
        else:
            print('Test is complite')

        if Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements() - 1, 6) != -1:
            for write in range(Memory_log.Number_Of_Elements()):
                if (Memory_log.Pick_Up_Single_Value(write, 6)) == (Memory_log.Pick_Up_Single_Value(write, 1)):
                    print('Совпадает')
                    self.update = int(
                        Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) + 5

                    if self.update >= 100:
                        self.update = 100
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True
                else:
                    print('Несовпадает')
                    self.update = int(Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) - 5
                    if self.update <= 0:
                        self.update = 0
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True

        else:
            pass
        Base_Est.Close_Database()
        Memory_log.Close_Database()

    # ----------------------------------------------------------------------------

    def answer_checking_RB(self):
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        for find in range(0, Memory_log.Number_Of_Elements()):
            if Memory_log.Pick_Up_Single_Value(find, 7) == '0':
                position = find - 1
                break
            elif find == Memory_log.Number_Of_Elements() - 1:
                position = Memory_log.Number_Of_Elements() - 1
                self.ids.QUE_WORD.text = 'Test is complite'
                Memory_log.Print_Data()





            else:
                find += 1
                # print('find', find)

        if Memory_log.Pick_Up_Single_Value(position, 6) == -1 and Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements()-1,6) == -1:
            LBL = Memory_log.Pick_Up_Single_Value(position, 1)
            RT = Memory_log.Pick_Up_Single_Value(position, 2)
            RB = Memory_log.Pick_Up_Single_Value(position, 3)
            LT = Memory_log.Pick_Up_Single_Value(position, 4)
            LB = Memory_log.Pick_Up_Single_Value(position, 5)

            if LBL == RB:
                self.ids.RB.background_color = (0, 1, 0, 0.8)
            else:
                self.ids.RB.background_color = (1, 0, 0, 0.8)

            if RT == LBL:
                self.ids.RT.background_color = (0, 1, 0, 0.8)
            else:
                if LT == LBL:
                    self.ids.LT.background_color = (0, 1, 0, 0.8)
                else:
                    if LB == LBL:
                        self.ids.LB.background_color = (0, 1, 0, 0.8)

            Memory_log.Update_ans_value(position + 1, Memory_log.Pick_Up_Single_Value(position, 3))

            Memory_log.Print_Data()
        else:
            print('Test is complite')

        if Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements() - 1, 6) != -1:
            for write in range(Memory_log.Number_Of_Elements()):
                if (Memory_log.Pick_Up_Single_Value(write, 6)) == (Memory_log.Pick_Up_Single_Value(write, 1)):
                    print('Совпадает')
                    self.update = int(
                        Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) + 5

                    if self.update >= 100:
                        self.update = 100
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True
                else:
                    print('Несовпадает')
                    self.update = int(Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) - 5
                    if self.update <= 0:
                        self.update = 0
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True

        else:
            pass

        Base_Est.Close_Database()
        Memory_log.Close_Database()

    # ----------------------------------------------------------------------------

    def answer_checking_LT(self):
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        for find in range(0, Memory_log.Number_Of_Elements()):
            if Memory_log.Pick_Up_Single_Value(find, 7) == '0':
                position = find - 1
                break
            elif find == Memory_log.Number_Of_Elements() - 1:
                position = Memory_log.Number_Of_Elements() - 1
                self.ids.QUE_WORD.text = 'Test is complite'
                Memory_log.Print_Data()

            else:
                find += 1
                # print('find', find)
        if Memory_log.Pick_Up_Single_Value(position, 6) == -1 and Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements()-1,6) == -1:

            LBL = Memory_log.Pick_Up_Single_Value(position, 1)
            RT = Memory_log.Pick_Up_Single_Value(position, 2)
            RB = Memory_log.Pick_Up_Single_Value(position, 3)
            LT = Memory_log.Pick_Up_Single_Value(position, 4)
            LB = Memory_log.Pick_Up_Single_Value(position, 5)

            if LBL == LT:
                self.ids.LT.background_color = (0, 1, 0, 0.8)
            else:
                self.ids.LT.background_color = (1, 0, 0, 0.8)

            if RB == LBL:
                self.ids.RB.background_color = (0, 1, 0, 0.8)
            else:
                if RT == LBL:
                    self.ids.RT.background_color = (0, 1, 0, 0.8)
                else:
                    if LB == LBL:
                        self.ids.LB.background_color = (0, 1, 0, 0.8)

            Memory_log.Update_ans_value(position + 1, Memory_log.Pick_Up_Single_Value(position, 4))
            Memory_log.Print_Data()
        else:
            print('Test is complite')

        if Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements() - 1, 6) != -1:
            for write in range(Memory_log.Number_Of_Elements()):
                if (Memory_log.Pick_Up_Single_Value(write, 6)) == (Memory_log.Pick_Up_Single_Value(write, 1)):
                    print('Совпадает')
                    self.update = int(
                        Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) + 5

                    if self.update >= 100:
                        self.update = 100
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True
                else:
                    print('Несовпадает')
                    self.update = int(Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) - 5
                    if self.update <= 0:
                        self.update = 0
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True

        else:
            pass
        Base_Est.Close_Database()
        Memory_log.Close_Database()

    # ----------------------------------------------------------------------------

    def answer_checking_LB(self):
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')

        # Finding position
        for find in range(0, Memory_log.Number_Of_Elements()):
            if Memory_log.Pick_Up_Single_Value(find, 7) == '0':
                position = find - 1
                break
            elif find == Memory_log.Number_Of_Elements() - 1:
                position = Memory_log.Number_Of_Elements() - 1
                self.ids.QUE_WORD.text = 'Test is complite'
                Memory_log.Print_Data()





            else:
                find += 1
                # print('find', find)

        if Memory_log.Pick_Up_Single_Value(position, 6) == -1 and Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements()-1,6) == -1:
            LBL = Memory_log.Pick_Up_Single_Value(position, 1)
            RT = Memory_log.Pick_Up_Single_Value(position, 2)
            RB = Memory_log.Pick_Up_Single_Value(position, 3)
            LT = Memory_log.Pick_Up_Single_Value(position, 4)
            LB = Memory_log.Pick_Up_Single_Value(position, 5)

            if LBL == LB:
                self.ids.LB.background_color = (0, 1, 0, 0.8)
            else:
                self.ids.LB.background_color = (1, 0, 0, 0.8)

            if RB == LBL:
                self.ids.RB.background_color = (0, 1, 0, 0.8)
            else:
                if LT == LBL:
                    self.ids.LT.background_color = (0, 1, 0, 0.8)
                else:
                    if RT == LBL:
                        self.ids.RT.background_color = (0, 1, 0, 0.8)

            Memory_log.Update_ans_value(position + 1, Memory_log.Pick_Up_Single_Value(position, 5))
            Memory_log.Print_Data()

        else:
            print('Test is complite')

        if Memory_log.Pick_Up_Single_Value(Memory_log.Number_Of_Elements() - 1, 6) != -1:
            for write in range(Memory_log.Number_Of_Elements()):
                if (Memory_log.Pick_Up_Single_Value(write, 6)) == (Memory_log.Pick_Up_Single_Value(write, 1)):
                    print('Совпадает')
                    self.update = int(
                        Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) + 5

                    if self.update >= 100:
                        self.update = 100
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True
                else:
                    print('Несовпадает')
                    self.update = int(Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3)) - 5
                    if self.update <= 0:
                        self.update = 0
                    else:
                        pass
                    print('word ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 1))))
                    print('was ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    Base_Est.Update_progress_value(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0), self.update)
                    print('Become ' + str(
                        (Base_Est.Pick_Up_Single_Value(Memory_log.Pick_Up_Single_Value(write, 1), 3))))
                    print('Ячейка' + str(
                        Base_Est.Pick_Up_Single_Value(int(Memory_log.Pick_Up_Single_Value(write, 1)), 0)))
                    self.ids.RT.disabled = True
                    self.ids.RB.disabled = True
                    self.ids.LT.disabled = True
                    self.ids.LB.disabled = True

        else:
            pass

        Base_Est.Close_Database()
        Memory_log.Close_Database()

    # ----------------------------------------------------------------------------

    def forward(self):
        Base_Est = Create_cursor('eng_rus.db')
        Memory_log = Create_cursor('log.db')
        # Finding position
        position = 0
        pos = 1
        for find in range(0, Memory_log.Number_Of_Elements()):
            if Memory_log.Pick_Up_Single_Value(find, 7) == '0':
                position = find
                # print('position=', position)
                break
            elif find == Memory_log.Number_Of_Elements() - 1:
                position = Memory_log.Number_Of_Elements() - 1
                print(position)
                break

            else:
                find += 1
                print('positon=', find)

        if position <= Memory_log.Number_Of_Elements() - 1 and Memory_log.Pick_Up_Single_Value(position,6) == -1 and Memory_log.Pick_Up_Single_Value(position - 1, 6) != -1:
            LBL = Memory_log.Pick_Up_Single_Value(position, 1)
            RT = Memory_log.Pick_Up_Single_Value(position, 2)
            RB = Memory_log.Pick_Up_Single_Value(position, 3)
            LT = Memory_log.Pick_Up_Single_Value(position, 4)
            LB = Memory_log.Pick_Up_Single_Value(position, 5)
            ANS = Memory_log.Pick_Up_Single_Value(position - 1, 6)

            self.ids.QUE_WORD.text = Base_Est.Pick_Up_Single_Value(LBL, 1)
            self.ids.RT.text = Base_Est.Pick_Up_Single_Value(RT, 2)
            self.ids.RB.text = Base_Est.Pick_Up_Single_Value(RB, 2)
            self.ids.LT.text = Base_Est.Pick_Up_Single_Value(LT, 2)
            self.ids.LB.text = Base_Est.Pick_Up_Single_Value(LB, 2)
            self.ids.RT.background_color = (1, 1, 1, 0.8)
            self.ids.RB.background_color = (1, 1, 1, 0.8)
            self.ids.LT.background_color = (1, 1, 1, 0.8)
            self.ids.LB.background_color = (1, 1, 1, 0.8)
            Memory_log.Update_position_value(position + 1, 1)
            Memory_log.Print_Data()
        else:

            print('Test is complite')

        Base_Est.Close_Database()
        Memory_log.Close_Database()

    # ----------------------------------------------------------------------------

    def back_function(self):
        self.ids.RT.background_color = (1, 1, 1, 0.8)
        self.ids.RB.background_color = (1, 1, 1, 0.8)
        self.ids.LT.background_color = (1, 1, 1, 0.8)
        self.ids.LB.background_color = (1, 1, 1, 0.8)


class Add_Word(Screen):

    def add_to_base(self):
        eng = self.ids.ENG_WORD.text
        rus = self.ids.RUS_WORD.text
        Progress = 10
        Time = Now_Time()
        word = {'Eng_word': eng, 'Translation': rus, 'Progress': Progress, 'Time': Time}

        Base_Est = Create_cursor('eng_rus.db')
        Base_Est.Create_Table()
        Base_Est.Write_New_Word(word)

    def hello(self):
        print('hello')


class Dictionary(Screen):

    def __init__(self,**kwargs):
        super(Dictionary,self).__init__(**kwargs)
        self.Base_Est = ''
        self.root = ScrollView(size_hint=(1, 1))
        #self.root.pos_hint = {'x': 0, 'top': 0.6}

        self.top_layout = GridLayout()
        self.top_layout.bind(minimum_height=self.top_layout.setter("height"))
        
        

        self.top_layout.size_hint_y = None
        self.top_layout.size_hint_x = 1

        self.word_box = []
        self.button_box = []
        self.sector_box=[]

        self.button_edit = []
        self.button_remove = []
        self.lbl_word = []
        self.lbl_translate = []
        self.lbl_procent = []
        self.lbl_elem_num = ''


    def on_pre_enter(self, *args):
        self.Base_Est = ''
        self.root = ScrollView(size_hint=(1, 0.85))
        self.root.pos_hint = {'x': 0, 'top': 1}

        self.top_layout = GridLayout()
        self.top_layout.bind(minimum_height=self.top_layout.setter("height"))
        self.top_layout.cols = 1
        

        self.top_layout.size_hint_y = None
        self.top_layout.size_hint_x = 1

        self.word_box = []
        self.button_box = []
        self.sector_box =[]

        self.button_edit = []
        self.button_remove = []
        self.lbl_word = []
        self.lbl_translate = []
        self.lbl_procent = []
        self.lbl_elem_num = ''
        self.Base_Est = Create_cursor('eng_rus.db')
        self.Base_Est.Create_Table()

        self.lbl_elem_num = Label(text='Количество слов в словаре ' + str(self.Base_Est.Number_Of_Elements()),size_hint_x=0.7, size_hint_y=None, height=30,font_size=32)
        self.top_layout.add_widget(self.lbl_elem_num)

        for but_number in range(self.Base_Est.Number_Of_Elements()):
            self.lbl_word.append(
                Label(text=str(self.Base_Est.Pick_Up_Single_Value(but_number, 1)), size_hint_x=1, size_hint_y=None,
                      height=120, font_size=72))
            self.lbl_translate.append(
                Label(text=str(self.Base_Est.Pick_Up_Single_Value(but_number, 2)), size_hint_x=1, size_hint_y=None,
                      height=120, font_size=72))
            self.lbl_procent.append(
                Label(text='изучено ' + str(self.Base_Est.Pick_Up_Single_Value(but_number, 3)) + '%', size_hint_x=1,
                      size_hint_y=None, height=70, font_size=40,halign="center", valign="bottom" ,color=[1,0,1,1]))

            self.word_box.append(BoxLayout(orientation='horizontal', size_hint_x=1, size_hint_y=None, height=120))
            self.button_box.append(BoxLayout(orientation='horizontal', size_hint_x=1, size_hint_y=None, height=120))
            self.sector_box.append(BoxLayout(orientation='vertical', size_hint_x=0.5, size_hint_y=None, height=350, padding=[30,30,30,30]))


            self.word_box[but_number].add_widget(self.lbl_word[but_number])
            self.word_box[but_number].add_widget(self.lbl_translate[but_number])

            self.button_edit.append(Button(text='Редактировать', size_hint_x=0.5, size_hint_y=None, height=100, background_color=[0,1,1,1]))
            self.button_edit[but_number].bind(on_release=partial(self.save, but_number))
            self.button_remove.append(Button(text='Удалить', size_hint_x=0.5, size_hint_y=None, height=100, background_color=[0,1,1,1]))
            self.button_remove[but_number].bind(on_release=partial(self.remove, but_number))

            self.button_box[but_number].add_widget(self.button_edit[but_number])
            self.button_box[but_number].add_widget(self.button_remove[but_number])

            self.sector_box[but_number].add_widget(self.word_box[but_number])
            self.sector_box[but_number].add_widget(self.lbl_procent[but_number])
            self.sector_box[but_number].add_widget(self.button_box[but_number])
            
            
            
            self.top_layout.add_widget(self.sector_box[but_number])



        self.root.add_widget(self.top_layout)
        self.add_widget(self.root)

        self.Base_Est.Close_Database()


    def save(self, but_number,*args):
        self.poppit = str(but_number)
        self.save_popup = SaveDialog(self)
        self.save_popup.open()



    def remove(self, but_number,*args):
        print('removed element '+str(but_number))
        self.Base_Est = Create_cursor('eng_rus.db')
        print(self.Base_Est.Pick_Up_Single_Value(but_number, 0))


        self.remove_widget(self.root)
        self.Base_Est.Delete_Record(self.Base_Est.Pick_Up_Single_Value(but_number,0))
        self.on_pre_enter()
        self.Base_Est.Close_Database()



    def back_function(self):
        self.remove_widget(self.root)


class SaveDialog(Popup):


    def __init__(self,my_widget,**kwargs):  # my_widget is now the object where popup was called from.
        super(SaveDialog,self).__init__(**kwargs)


        self.size_hint = (0.7, 0.38)
        self.title = ''
        self.auto_dismiss = False
        self.my_widget = my_widget
        self.Base_Est = Create_cursor('eng_rus.db')
        self.Memory_log = Create_cursor('log.db')
        self.Time=''
        print(self.Base_Est.Pick_Up_Single_Value(int(self.my_widget.poppit), 3))
        self.Base_Est.Print_Data()
        self.word = self.Base_Est.Pick_Up_Single_Value(int(self.my_widget.poppit), 1)
        self.translate = self.Base_Est.Pick_Up_Single_Value(int(self.my_widget.poppit), 2)
        self.progress = self.Base_Est.Pick_Up_Single_Value(int(self.my_widget.poppit), 3)
        self.start_progress = int(self.progress)
        self.progress_value = int(self.progress)
        self.start_value = 'Прогресс слова ' + str(self.progress_value) + '%'

        self.slide_text = 'Прогресс слова'
        
        self.main_boxlayout = BoxLayout(orientation="vertical" )
        self.text_boxlayout = BoxLayout(orientation="vertical",size_hint_y=0.75)
        self.button_layout = BoxLayout(orientation="horizontal",size_hint_y=0.15)

        self.text_input_word = TextInput(text=self.word,size_hint_x=1, size_hint_y=0.17, height=45,font_size=68, multiline=False)
        self.text_input_translate = TextInput(text=self.translate, size_hint_x=1,size_hint_y=0.17, height=45,font_size=68, multiline=False)
        self.word_lbl = Label(text='Word', size_hint_x=1, size_hint_y=0.13, height=30, font_size=48)
        self.translate_lbl = Label(text='Translation', size_hint_x=1,size_hint_y=0.13, height=30, font_size=48)
        self.progress = Label(text=self.start_value, halign="center", valign="bottom",size_hint_x=1, size_hint_y=0.2, height=40, font_size=48)
        self.slid = Slider(min=0, max=100, step=5, size_hint_y=0.2, height=50, value=self.progress_value)
        self.slid.bind(value=self.on_value_change)

        self.text_boxlayout.add_widget(self.word_lbl)
        self.text_boxlayout.add_widget(self.text_input_word)
        self.text_boxlayout.add_widget(self.translate_lbl)     
        self.text_boxlayout.add_widget(self.text_input_translate)
        self.text_boxlayout.add_widget(self.progress)
        self.text_boxlayout.add_widget(self.slid)


        
        self.save_button = Button(text='Accept',size_hint_y=1)
        self.save_button.bind(on_press=self.save)

        self.cancel_button = Button(text='Cancel',size_hint_y=1)
        self.cancel_button.bind(on_press=self.cancel)

        self.button_layout.add_widget(self.save_button)
        self.button_layout.add_widget(self.cancel_button)

        self.main_boxlayout.add_widget(self.text_boxlayout)
        self.main_boxlayout.add_widget(self.button_layout)
        self.add_widget(self.main_boxlayout)


    def on_value_change(self,*args):
        self.progress_value = int(args[1])
        self.progress.text = 'Прогресс слова '+str(int(args[1]))+'%'

    def save(self,*args):
        #self.my_widget.poppit = self.Base_Est.Pick_Up_Single_Value(self.my_widget.poppit, 0)
        self.Base_rows_id = self.Base_Est.Pick_Up_Single_Value(int(self.my_widget.poppit), 0)
        self.Base_Est.Update_word_value(int(self.Base_rows_id), self.text_input_word.text)
        self.Base_Est.Update_translate_value(int(self.Base_rows_id), self.text_input_translate.text)
        self.Base_Est.Update_progress_value(int(self.Base_rows_id), self.progress_value)
        if self.progress_value == 100 and self.start_progress != 100:
            self.Time = Now_Time()
            print(self.Time)
            self.Base_Est.Update_time_value(int(self.Base_rows_id) + 1, self.Time)
        else:
            pass

        self.my_widget.lbl_word[int(self.my_widget.poppit)].text = self.text_input_word.text
        self.my_widget.lbl_translate[int(self.my_widget.poppit)].text = self.text_input_translate.text
        self.my_widget.lbl_procent[int(self.my_widget.poppit)].text = 'изучено ' + str(int(self.progress_value)) + '%'



        self.Base_Est.Close_Database()
        self.Memory_log.Close_Database()

        self.dismiss()

    def cancel(self,*args):
        print ("cancel")
        self.Base_Est.Close_Database()
        self.Memory_log.Close_Database()
        self.dismiss()


class Caution(Popup):

    def __init__(self, my_widget,**kwargs):  # my_widget is now the object where popup was called from.
        super(Caution, self).__init__(**kwargs)

        self.size_hint = (0.6, 0.40)
        self.title = ''
        self.auto_dismiss = False
        self.my_widget = my_widget

        self.Base_Est = Create_cursor('eng_rus.db')
        self.Memory_log = Create_cursor('log.db')


        self.main_boxlayout = BoxLayout(orientation="vertical")
        self.lbl_boxlayout = BoxLayout(orientation="vertical")
        self.button_layout = BoxLayout(orientation="vertical", size_hint_y=0.20)

        self.word_lbl = Label(text='Слов для тестирования слишком мало.\nПожалуйста довавьте еще слов.', size_hint_y=0.8, height=180, halign="center", valign="middle", font_size=54)
        self.word_lbl.bind(size=self.word_lbl.setter('text_size'))
        self.cancel_button = Button(text='Cancel', size_hint_y=1)
        self.cancel_button.bind(on_press=self.cancel)


        self.lbl_boxlayout.add_widget(self.word_lbl)
        self.button_layout.add_widget(self.cancel_button)

        self.main_boxlayout.add_widget(self.lbl_boxlayout)
        self.main_boxlayout.add_widget(self.button_layout)
        self.add_widget(self.main_boxlayout)

    def cancel(self, *args):

        print("cancel")
        self.Base_Est.Close_Database()
        self.Memory_log.Close_Database()
        print(self.my_widget)
        self.dismiss()


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('all.kv')


class AwesomeApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    AwesomeApp().run()
