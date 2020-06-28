import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QDate
import auto_cal

# Data Insert
data = []

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("auto.ui")[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 숙박 체크박스 기능을 연결하는 코드
        # m_btn : 모텔 // h_btn : 호텔 // p_btn : 펜션 // r_btn : 리조트 // g_btn : 게스트 // c_btn : 캠핑 // k_btn : 한
        self.m_btn.clicked.connect(self.stateFunc)
        self.h_btn.clicked.connect(self.stateFunc)
        self.p_btn.clicked.connect(self.stateFunc)
        self.r_btn.clicked.connect(self.stateFunc)
        self.g_btn.clicked.connect(self.stateFunc)
        self.c_btn.clicked.connect(self.stateFunc)
        self.k_btn.clicked.connect(self.stateFunc)

        # 대실, 숙박기능은 연결하는 코드
        # kl_btn : 대실 // l_btn : 숙박
        self.kl_btn.clicked.connect(self.chkFunc)
        self.l_btn.clicked.connect(self.chkFunc)

        # 날짜 기능을 연결하는 코드
        # checkIn Date
        self.c_in.setDate(QDate.currentDate())
        self.c_in.setCalendarPopup(True)

        # checkOut Date
        self.c_out.setDate(QDate.currentDate())
        self.c_out.setCalendarPopup(True)

        # check & call Function
        self.startBtn.clicked.connect(self.goFunction)

    def stateFunc(self):
        # 1:모텔 // 2:호텔 // 3:펜션 //4:리조트 // 5:게스트하우스 // 6:캠핑 // 7: 한옥
        if self.m_btn.isChecked(): self.accomdation = "1"
        if self.h_btn.isChecked(): self.accomdation = "2"
        if self.p_btn.isChecked(): self.accomdation = "3"
        if self.r_btn.isChecked(): self.accomdation = "4"
        if self.g_btn.isChecked(): self.accomdation = "5"
        if self.c_btn.isChecked(): self.accomdation = "6"
        if self.k_btn.isChecked(): self.accomdation = "7"

    def chkFunc(self):
        # 1: 대실 2:숙박
        if self.kl_btn.isChecked(): self.state = "1"
        if self.l_btn.isChecked(): self.state = "2"

    def goFunction(self, count):
        acc_inf     = self.accomdation
        if acc_inf == "1": tm_acc_inf = "모텔"
        if acc_inf == "2": tm_acc_inf = "호텔"
        if acc_inf == "3": tm_acc_inf = "펜션"
        if acc_inf == "4": tm_acc_inf = "리조트"
        if acc_inf == "5": tm_acc_inf = "게스트하우스"
        if acc_inf == "6": tm_acc_inf = "캠핑/글램핑"
        if acc_inf == "7": tm_acc_inf = "한옥"

        state_inf   = self.state
        if state_inf == "1": tm_state = "대실"
        if state_inf == "2": tm_state = "숙박"

        l_inf      = self.l_inf.text()
        r_inf = self.r_inf.text()
        if not l_inf.isdecimal() or not r_inf.isdecimal():
            QMessageBox.about(self, "Error", "숫자입력해주세요")

        else:
            in_inf      = self.c_in.text()
            tmp_checkIn = in_inf.split("/")
            tmp_checkIn = list(reversed(tmp_checkIn))
            checkIn = "".join(tmp_checkIn)

            out_inf     = self.c_out.text()
            tmp_checkOut = out_inf.split("/")
            tmp_checkOut = list(reversed(tmp_checkOut))
            checkOut = "".join(tmp_checkOut)

            data.append((tm_acc_inf, tm_state, l_inf, r_inf, checkIn, checkOut))

            row = 0
            count = 1
            for r_data in data:
                col = 0

                for item in r_data:
                    cellinfo = QTableWidgetItem(item)
                    self.data_view.setRowCount(count)
                    self.data_view.setItem(row,col,cellinfo)
                    col+=1
                row += 1
                count += 1

            auto_cal.automate_program(acc_inf, state_inf, l_inf, r_inf, checkIn, checkOut)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
