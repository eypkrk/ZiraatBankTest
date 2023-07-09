from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from datetime import date

class TestZiraat:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.ziraatbank.com.tr")
        self.driver.maximize_window()
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        btnCls = self.driver.find_element(By.XPATH,"/html/body/div[2]/a")
        btnCls.click()
        
   
    def teardown_method(self):
        self.driver.quit()

    def wait(self,locator):
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((locator)))
    def scrollTo(self,scroll):
        self.driver.execute_script(f"window.scrollTo(0,{scroll})")
    def action(self,btn):
        actions = ActionChains(self.driver)
        actions.move_to_element(btn).perform()
    #bireysel
    def test_pers(self):
        self.wait((By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[1]/a"))
        for i in range(1,5):
            sleep(2)
            btnPers = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[1]/a")
            self.action(btnPers)
            btnMevduat = self.driver.find_element(By.XPATH,f"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[1]/div/div/div/div[1]/ul/li[{i}]/a")
            btnMevduat.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/1.png")
            self.driver.back()
            if (i >= 4):
                j = 2
                for i in range(1,4):
                    btnPers = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[1]/a")
                    self.action(btnPers)
                    btnMevduat = self.driver.find_element(By.XPATH,f"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[1]/div/div/div/div[{j}]/ul/li[{i}]/a")
                    btnMevduat.click()
                    self.scrollTo(200)
                    self.driver.save_screenshot(f"{self.folderPath}/1-{i}.png")
                    self.driver.back()
    #Ticari
    def test_commer(self):
        self.wait((By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[2]/a"))
        for i in range(1,6):
            btnCommercial = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[2]/a")
            self.action(btnCommercial)
            btnCommerBottom = self.driver.find_element(By.XPATH,f"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[2]/div/div/div/div[1]/ul/li[{i}]/a")
            btnCommerBottom.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/2.png")
            self.driver.back()
            if (i >= 5):
                j = 2
                for i in range(1,6): 
                    btnCommercial = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[2]/a")
                    self.action(btnCommercial)
                    btnCommerBottom = self.driver.find_element(By.XPATH,f"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[2]/div/div/div/div[{j}]/ul/li[{i}]/a")
                    btnCommerBottom.click()
                    self.scrollTo(200)
                    self.driver.save_screenshot(f"{self.folderPath}/2-{i}")
                    self.driver.back()

    #Kurumsal
    def test_institutional(self):
        self.wait((By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[3]/a"))
        for i in range(1,6):
            btnInstitutional = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[3]/a")
            self.action(btnInstitutional)
            btnCommercial = self.driver.find_element(By.XPATH,f"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[3]/div/div/div/div[1]/ul/li[{i}]/a")
            btnCommercial.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/3.png")
            self.driver.back()
            if(i >= 5):
                j = 2
                for i in range(1,5):
                    btnInstitutional = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[3]/a")
                    self.action(btnInstitutional)
                    btnCommercial = self.driver.find_element(By.XPATH,f"//*[@id='slider-container']/header/div[2]/div[2]/nav/ul/li[3]/div/div/div/div[{j}]/ul/li[{i}]/a")
                    btnCommercial.click()
                    self.scrollTo(200)
                    self.driver.save_screenshot(f"{self.folderPath}/3-{i}")
                    self.driver.back()
    #kartlar
    def test_card(self):
        btnCard = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/a[1]")
        btnCard.click()
        self.scrollTo(300)
        self.driver.save_screenshot(f"{self.folderPath}/4.png")

        for i in range(1,4):
            self.wait((By.XPATH,"//*[@id='landingNavBireysel']/div[2]/div[1]/div"))
            btnCardOfCredit = self.driver.find_element(By.XPATH,f"//*[@id='landingNavBireysel']/div[2]/div[1]/div/ul/li[{i}]/a")
            btnCardOfCredit.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/4-{i}.png")
            self.driver.back()
            sleep(1)

        for j in range(1,3):
            self.wait((By.XPATH,"//*[@id='landingNavBireysel']/div[2]/div[2]/div"))
            btnCardOfBank = self.driver.find_element(By.XPATH,f"//*[@id='landingNavBireysel']/div[2]/div[2]/div/ul/li[{j}]/a")
            btnCardOfBank.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/4-{i}-{j}.png")
            self.driver.back()

        btnCardOfYoung = self.driver.find_element(By.XPATH,"//*[@id='landingNavBireysel']/div[2]/div[3]/div/a")
        btnCardOfYoung.click()
        self.driver.back()

        for k in range(1,4):
            btnCards = self.driver.find_element(By.XPATH,f"//*[@id='landingNavBireysel']/div[3]/div[{k}]/div/a")
            btnCards.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/4-{i}-{j}-{k}.png")
            self.driver.back()

        self.scrollTo(800)
        
        for l in range(1,3):
            self.wait((By.XPATH,f"//*[@id='landingNavTicari']/div[2]/div[1]/div/div/div[1]/ul/li[{l}]/a"))
            btnCardOfBasak = self.driver.find_element(By.XPATH,f"//*[@id='landingNavTicari']/div[2]/div[1]/div/div/div[1]/ul/li[{l}]/a")
            btnCardOfBasak.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/4-{i}-{j}-{k}-{l}.png")
            self.driver.back()

        btnBusiness = self.driver.find_element(By.XPATH,"//*[@id='landingNavTicari']/div[2]/div[2]/div/div/div[2]/a")
        btnBusiness.click()
        self.scrollTo(200)
        self.driver.save_screenshot(f"{self.folderPath}/4son.png")
        self.driver.back()
   
    #süper şube
    def test_super(self):
        self.wait((By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/a[2]"))
        btnSuper = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/a[2]")
        btnSuper.click()
        self.scrollTo(100)
        self.driver.save_screenshot(f"{self.folderPath}/5.png")
        for i in range(1,3):
            btnSupers = self.driver.find_element(By.XPATH,f"//*[@id='landingNav']/div/div[{i}]")
            btnSupers.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/5-{i}.png")
            self.driver.back()
    #arama butonu
    def test_search(self):
        btnSearch = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/div[1]/a")
        self.action(btnSearch)
        btnTxtArea = self.driver.find_element(By.ID,"searchTxt")
        btnTxtArea.send_keys("kyk kredi")
        self.driver.save_screenshot(f"{self.folderPath}/6.png")
        btnTxtArea.send_keys(Keys.ENTER)
        self.scrollTo(200)
        btnLink1 = self.driver.find_element(By.ID,"ctl00_ctl45_g_f3076583_9120_40a9_9ceb_034c6154b9e2_csr6_item_itemTitleLink")
        btnLink1.click()
        self.scrollTo(200)
        self.driver.save_screenshot(f"{self.folderPath}/6-1.png")
        self.driver.back()
        self.wait((By.ID,"ctl00_ctl45_g_f3076583_9120_40a9_9ceb_034c6154b9e2_csr7_item_itemTitleLink"))
        self.scrollTo(200)
        btnLink2 = self.driver.find_element(By.ID,"ctl00_ctl45_g_f3076583_9120_40a9_9ceb_034c6154b9e2_csr7_item_itemTitleLink")
        btnLink2.click()
        self.scrollTo(200)
        self.driver.save_screenshot(f"{self.folderPath}/6-2.png")
        self.driver.back()
    
    #internet şubesi bireysel
    def test_internetPers(self):
        btnInternet = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/div[4]/a")
        self.action(btnInternet)
        btnPers = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/div[4]/div/a[1]")
        btnPers.click()
        self.driver.save_screenshot(f"{self.folderPath}/7.png")
    #internet şubesi kurumsal
    def testInternetInst(self):
        btnInternet = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/div[4]/a")
        self.action(btnInternet)
        btnInstitutional = self.driver.find_element(By.XPATH,"//*[@id='slider-container']/header/div[2]/div[2]/div[2]/div[4]/div/a[2]")
        btnInstitutional.click()
        self.driver.save_screenshot(f"{self.folderPath}/8.png")
        sleep(5)

    #slider

    def test_slider(self):
        for i in range(1,10):
            self.wait((By.XPATH,f"//*[@id='owl-controls-1']/div[2]/div[{i}]/span"))
            btnSlider = self.driver.find_element(By.XPATH,f"//*[@id='owl-controls-1']/div[2]/div[{i}]/span")
            btnSlider.click()
            sleep(1)
            j = 5
            if (i <= 5):
                j += i
                self.wait((By.XPATH,f"//*[@id='ContentSection']/div/div[1]/div[1]/div/div[{j}]/div/div/div/div[1]/a"))
                btnInf = self.driver.find_element(By.XPATH,f"//*[@id='ContentSection']/div/div[1]/div[1]/div/div[{j}]/div/div/div/div[1]/a")
                btnInf.click()
                sleep(1)
                self.driver.save_screenshot(f"{self.folderPath}/9-{i}.png")               
                self.driver.back()
            elif(i == 6):
                sleep(1)
                self.wait((By.XPATH,f"//*[@id='ContentSection']/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/a"))
                btnInf = self.driver.find_element(By.XPATH,f"//*[@id='ContentSection']/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/a")
                btnInf.click()
                sleep(1)
                self.driver.save_screenshot(f"{self.folderPath}/9-{i}")
                self.driver.back()

                

    
    #Anasayfa 2. bölüm(alt-satır)
    def test_bottomSlider(self):
        self.scrollTo(650)
        sleep(1)
        btnGeneralData = self.driver.find_element(By.XPATH,"//*[@id='main-box']/div/div/div[1]/div/div[1]/a[2]")
        btnGeneralData.click()
        
        #mevduatHesapla
        txtDay = self.driver.find_element(By.ID,"deposit-calc-vade")
        txtDay.clear()
        txtDay.send_keys("200")
        txtTotal = self.driver.find_element(By.ID,"tutar")
        txtTotal.clear()
        txtTotal.send_keys("25000")
        sleep(5)
        self.driver.save_screenshot(f"{self.folderPath}/10.png")

        #krediHesapla
        btnCredit = self.driver.find_element(By.XPATH,"//*[@id='calc-form-box']/div/div[1]/a[2]")
        btnCredit.click()
        txtCredit = self.driver.find_element(By.ID,"kredi-tutari")
        txtCredit.clear()
        txtCredit.send_keys("50000")
        txtMonthC = self.driver.find_element(By.ID,"calc-vade")
        txtMonthC.clear()
        txtMonthC.send_keys("36")
        sleep(5)
        self.driver.save_screenshot(f"{self.folderPath}/10-1.png")

        #başvurular->bireyselKredi
        btnPers = self.driver.find_element(By.ID,"home-icon-kredi")
        btnPers.click()
        self.scrollTo(200)
        txtTc = self.driver.find_element(By.ID,"tckn")
        txtTc.send_keys("112233445566")
        txtPhone = self.driver.find_element(By.ID,"phone2")
        txtPhone.send_keys("987654321")
        txtMonth = self.driver.find_element(By.ID,"calc-vade")
        txtMonth.send_keys("500")
        txtTot = self.driver.find_element(By.ID,"calc-tutar")
        txtTot.send_keys("100000")
        txtCome = self.driver.find_element(By.ID,"incomeCertificate")
        txtCome.send_keys("1000000")
        sleep(3)
        self.driver.save_screenshot(f"{self.folderPath}/10-2.png")
        self.driver.back()

        #başvurular->BankKart
        btnCardOfBank = self.driver.find_element(By.ID,"home-icon-kart")
        btnCardOfBank.click()
        self.scrollTo(200)
        txtTc = self.driver.find_element(By.ID,"tckn")
        txtTc.send_keys("112233445566")
        txtPhone = self.driver.find_element(By.ID,"phone2")
        txtPhone.send_keys("987654321")
        self.driver.save_screenshot(f"{self.folderPath}/10-3.png")
        self.driver.back()

        #basşvurular->sigorta
        btnApply = self.driver.find_element(By.ID,"home-icon-sigorta")
        self.action(btnApply)
        sleep(3)
        btnApply.click()
        self.scrollTo(100)
        for i in range(1,8):
            self.wait((By.XPATH,f"//*[@id='landingNav']/div[1]/div[1]/div/div/div[1]/ul/li[{i}]/a"))
            btnInsurance = self.driver.find_element(By.XPATH,f"//*[@id='landingNav']/div[1]/div[1]/div/div/div[1]/ul/li[{i}]/a")
            btnInsurance.click()
            self.scrollTo(100)
            sleep(2)
            self.driver.save_screenshot(f"{self.folderPath}/11-{i}.png")
            self.driver.back()
            if (i >= 7):
                j = 2
                for k in range(1,3):
                    btnInsurance = self.driver.find_element(By.XPATH,f"//*[@id='landingNav']/div[1]/div[{j}]/div/ul/li[{k}]/a")
                    btnInsurance.click()
                    sleep(2)
                    self.driver.save_screenshot(f"{self.folderPath}/11-{i}-{k}.png")
                    self.driver.back()
                    if (k >= 2):
                        self.scrollTo(650)
                        for l in range(1,4):
                            self.wait((By.XPATH,f"//*[@id='landingNav']/div[{j}]/div[1]/div/ul/li[{l}]/a"))
                            btnHomeIns = self.driver.find_element(By.XPATH,f"//*[@id='landingNav']/div[{j}]/div[1]/div/ul/li[{l}]/a")
                            btnHomeIns.click()
                            sleep(2)
                            self.driver.save_screenshot(f"{self.folderPath}/11-{i}-{k}-{l}.png")
                            self.driver.back()
                            if(l >= 3):
                                for m in range(1,4):
                                    self.wait((By.XPATH,f"//*[@id='landingNav']/div[{j}]/div[{j}]/div/ul/li[{m}]/a"))
                                    btnHit = self.driver.find_element(By.XPATH,f"//*[@id='landingNav']/div[{j}]/div[{j}]/div/ul/li[{m}]/a")
                                    btnHit.click()
                                    sleep(2)
                                    self.driver.save_screenshot(f"{self.folderPath}/11-{i}-{k}-{l}-{m}.png")
                                    self.driver.back()
                                    if(m >= 3):
                                        for n in range(1,3):
                                            self.wait((By.XPATH,f"//*[@id='landingNav']/div[{j}]/div[3]/div/ul/li[{n}]/a"))
                                            btnResponsibility = self.driver.find_element(By.XPATH,f"//*[@id='landingNav']/div[{j}]/div[3]/div/ul/li[{n}]/a")
                                            btnResponsibility.click()
                                            sleep(2)
                                            self.driver.save_screenshot(f"{self.folderPath}/11-{i}-{k}-{l}-{m}-{n}.png")
                                            self.driver.back()
                                            if(n >= 2):
                                                #bireysel Emeklilik
                                                self.wait((By.XPATH,"//*[@id='landingNav']/div[3]/div[1]/div/ul/li/a"))
                                                btnOne = self.driver.find_element(By.XPATH,"//*[@id='landingNav']/div[3]/div[1]/div/ul/li/a")
                                                btnOne.click()
                                                sleep(2)
                                                self.driver.save_screenshot(f"{self.folderPath}/11-1-{i}-{k}-{l}-{m}-{n}.png")
                                                self.driver.back()
                                                for o in range(1,3):
                                                    self.wait((By.XPATH,"//*[@id='landingNav']/div[3]/div[2]/div/ul/li[1]/a"))
                                                    btnWife = self.driver.find_element(By.XPATH,f"//*[@id='landingNav']/div[3]/div[2]/div/ul/li[{o}]/a")
                                                    btnWife.click()
                                                    self.scrollTo(100)
                                                    sleep(2)
                                                    self.driver.save_screenshot(f"{self.folderPath}/11-{i}-{k}-{l}-{m}-{n}-{o}.png")
                                                    self.driver.back()
                                                self.driver.back()
                                                self.wait((By.ID,"home-icon-emeklilik"))
                                                btnRetired = self.driver.find_element(By.ID,"home-icon-emeklilik")  
                                                self.action(btnRetired)
                                                self.driver.save_screenshot(f"{self.folderPath}/11-2-{i}-{k}-{l}-{m}-{n}-{o}.png")
                                            
                                                btnCity = self.driver.find_element(By.XPATH,"//*[@id='main-box']/div/div/div[4]/div/div/div/div[2]/div[2]/div/span/span[1]/span")
                                                btnCity.click()
                                                btnTxt = self.driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
                                                btnTxt.send_keys("Gaziantep")
                                                self.driver.save_screenshot(f"{self.folderPath}/11-3-{i}-{k}-{l}-{m}-{n}-{o}.png")
                                                btnTxt.send_keys(Keys.ENTER)
                                                btnSearch = self.driver.find_element(By.XPATH,"//*[@id='main-box']/div/div/div[4]/div/div/div/div[2]/div[4]/a")
                                                btnSearch.click()
                                                self.scrollTo(300)
                                                sleep(2)
                                                self.driver.save_screenshot(f"{self.folderPath}/11-4-{i}-{k}-{l}-{m}-{n}-{o}.png")
                                                self.driver.back()
    #en alt kısım testi                                           
    def test_bottom(self):
        self.scrollTo(850)
        for i in range(1,4):
            self.wait((By.ID,"fnav1"))
            btnFinance = self.driver.find_element(By.ID,"fnav1")
            btnFinance.click()
            self.wait((By.XPATH,f"//*[@id='footer']/div/div/div[1]/div/ul[1]/li[1]/ul/li[{i}]/a"))
            btnIn = self.driver.find_element(By.XPATH,f"//*[@id='footer']/div/div/div[1]/div/ul[1]/li[1]/ul/li[{i}]/a")
            btnIn.click()
            self.scrollTo(100)
            sleep(2)
            self.driver.save_screenshot(f"{self.folderPath}/12-{i}.png")
            self.driver.back()
        self.scrollTo(850)
        self.wait((By.XPATH,"//*[@id='footer']/div/div/div[1]/div/ul[1]/li[3]/ul/li[1]/a"))
        btnCalc = self.driver.find_element(By.XPATH,"//*[@id='footer']/div/div/div[1]/div/ul[1]/li[3]/ul/li[1]/a")
        btnCalc.click()
        self.scrollTo(100)
        self.driver.save_screenshot(f"{self.folderPath}/12-1-2.png")
        self.wait((By.XPATH,"//*[@id='landingNav']/div[1]/div/div/div/div/div[1]/ul/li[1]/a"))
        btnCredit = self.driver.find_element(By.XPATH,"//*[@id='landingNav']/div[1]/div/div/div/div/div[1]/ul/li[1]/a")
        btnCredit.click()
        self.scrollTo(300)
        txtTot = self.driver.find_element(By.ID,"calc-tutar")
        txtTot.clear()
        txtTot.send_keys("50000")
        txtMonth = self.driver.find_element(By.ID,"calc-vade")
        txtMonth.clear()
        txtMonth.send_keys("36")
        txtPercent = self.driver.find_element(By.ID,"faiz-orani")
        txtPercent.send_keys("25")
        btnCalculator = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl45_g_5e92fe74_b9f1_4d33_87ec_33a2ed2d8ea5']/div/div/div[2]/div[2]/a")
        btnCalculator.click()
        self.scrollTo(100)
        self.driver.save_screenshot(f"{self.folderPath}/12-1-3.png")
        self.wait((By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/a"))
        btnCombo = self.driver.find_element(By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/a")
        btnCombo.click()
        self.driver.save_screenshot(f"{self.folderPath}/12-1-4.png")
        self.wait((By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/div/a[2]"))
        btnCar = self.driver.find_element(By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/div/a[2]")
        btnCar.click()
        sleep(2)
        self.driver.save_screenshot(f"{self.folderPath}/12-1-5.png")
        self.scrollTo(300)
        self.wait((By.XPATH,"//*[@id='ctl00_ctl45_g_84293f12_999c_49fb_8e66_2080461b8b59']/div/div/div[1]/div[1]/span/span[1]/span"))
        btnComboCar = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl45_g_84293f12_999c_49fb_8e66_2080461b8b59']/div/div/div[1]/div[1]/span/span[1]/span") 
        btnComboCar.click()
        self.driver.save_screenshot(f"{self.folderPath}/12-1-6.png")
        self.wait((By.ID,"select2-ddlCredit-results"))
        btnCarCredit = self.driver.find_element(By.ID,"select2-ddlCredit-results")
        self.action(btnCarCredit)
        btnCarCredit.click()
        self.driver.save_screenshot(f"{self.folderPath}/12-1-7.png")   
        txtTot = self.driver.find_element(By.ID,"calc-tutar")
        txtTot.clear()
        txtTot.send_keys("400000")
        txtMonth = self.driver.find_element(By.ID,"calc-vade")
        txtMonth.clear()
        txtMonth.send_keys("48")
        txtPercent = self.driver.find_element(By.ID,"faiz-orani")
        txtPercent.send_keys("50")   
        btnCalculat = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl45_g_84293f12_999c_49fb_8e66_2080461b8b59']/div/div/div[2]/div[2]/a") 
        btnCalculat.click()
        self.driver.save_screenshot(f"{self.folderPath}/12-1-8.png") 
        self.driver.back()
        self.wait((By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/a"))
        btnCombo = self.driver.find_element(By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/a")
        btnCombo.click()
        self.scrollTo(300)
        self.driver.save_screenshot(f"{self.folderPath}/12-1-9.png")
        self.wait((By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/div/a[3]"))
        btnHome = self.driver.find_element(By.XPATH,"//*[@id='ctl00_PlaceHolderMain_ctl04__ControlWrapper_RichHtmlField']/div[1]/div/a[3]")
        btnHome.click() 
        self.driver.save_screenshot(f"{self.folderPath}/12-1-10.png")
        btnComboHome = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl45_g_cc10f920_479e_4178_99f5_09c4d06318c5']/div/div/div[1]/div[1]/span/span[1]/span")
        btnComboHome.click()
        txtCombo = self.driver.find_element(By.XPATH,"/html/body/span/span/span[1]/input")
        txtCombo.send_keys("Konut Kredisi Ürün Paketi (2.000.000")
        self.driver.save_screenshot(f"{self.folderPath}/12-1-10.png")
        txtCombo.send_keys(Keys.ENTER)
        btnCalcu = self.driver.find_element(By.XPATH,"//*[@id='ctl00_ctl45_g_cc10f920_479e_4178_99f5_09c4d06318c5']/div/div/div[2]/div[2]/a")
        btnCalcu.click()

    def test_mapSite(self):
        self.scrollTo(850)
        sleep(2)
        self.wait((By.XPATH,"//*[@id='footer']/div/div/div[1]/div/ul[1]/li[3]/ul/li[3]/a"))
        btnMapSite = self.driver.find_element(By.XPATH,"//*[@id='footer']/div/div/div[1]/div/ul[1]/li[3]/ul/li[3]/a")
        btnMapSite.click()
        self.scrollTo(200)
        for i in range(1,11):
            btnCommercial = self.driver.find_element(By.XPATH,f"//*[@id='ctl00_ctl45_g_bf7d5bba_8767_4a65_b06b_9060c8c0ecc0']/div/div[1]/ul/li[{i}]/a")
            btnCommercial.click()
            self.scrollTo(200)
            self.driver.save_screenshot(f"{self.folderPath}/13-{i}.png")
        # btnCarCredit = self.driver.find_element(By.ID,"select2-ddlCredit-results")
        # self.action(btnCarCredit)
        # btnGreenCredit = self.driver.find_element(By.ID,"select2-ddlCredit-result-f1gx-TAŞY1")  
        # btnGreenCredit.click()



        # btnPers.send_keys(Keys.ALT+Keys.TAB) Konut Kredisi Ürün Paketi (2.000.000
        # sleep(2)
        # self.wait((By.ID,"ctl00_c_RetailIdentityContainer"))
        # txtTc = self.driver.find_element(By.ID,"ctl00_c_RetailIdentityContainer")
        # txtTc.send_keys(" ")
        # txtPassword = self.driver.find_element(By.ID,"ctl00_c_RetailPinTextBox")
        # txtPassword.send_keys(" ")
        # btnLgn = self.driver.find_element(By.ID,"ctl00_c_RetailLoginButton")
        # btnLgn.click()
        # txtError = self.driver.find_element(By.ID,"ctl00_c_RetailIdentityTextBox-error")
        # txtMsg = self.driver.find_element(By.ID,"ctl00_c_RetailPinTextBox-error")
        # assert txtError.text == "Müşteri / T.C. Kimlik Numaranızı Giriniz."
        # assert txtMsg.text == "Lütfen şifrenizi giriniz."