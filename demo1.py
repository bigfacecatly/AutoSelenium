import selenium
from selenium import webdriver
import time,os


#控制间隔时间
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
file_path = os.path.dirname(__file__)



#登陆
def login():
    driver = webdriver.Chrome(file_path+r'/chromedriver')
    driver.get('')
    login_name = driver.find_element_by_id('login_username')
    time.sleep(a)
    login_name.send_keys('test')
    login_passwd = driver.find_element_by_id('login_password')
    time.sleep(a)
    login_passwd.send_keys('test')
    time.sleep(a)
    submit = driver.find_element_by_tag_name('button')
    submit.click()
    return driver

#搜索项目
def clickSearch(driver):
    time.sleep(0.1)
    search_input = driver.find_element_by_tag_name('input')
    # search_input.send_keys('卡罗拉DEMO_新编辑器模式')
    search_input.send_keys('卡卡西')#卡罗拉DEMO_新编辑器模式
    time.sleep(a)
    search_input.send_keys(Keys.ENTER)
    return driver

#进入项目
def goProjectGroup(driver):
    time.sleep(0.1)
    project_group = driver.find_element_by_class_name('aw-prjct-card')
    project_group.click()
    return driver


#新建章节 message 章节名称,messageAlias章节别名,messageDecsription简介
def makeProjectGroup(driver,message,messageAlias,messageDecsription):
    # new_project = driver.find_elements_by_class_name("ant-page-header-heading-extra")[0]
    time.sleep(0.5)
    # input('232443')
    new_project = driver.find_elements_by_tag_name('button')[1]
    new_project.click()



    name_click = driver.find_element_by_id("new-project_project_name")
    name_click.send_keys(message)
    name_alias = driver.find_element_by_id("new-project_project_alias")
    name_alias.send_keys(messageAlias)
    name_decsription = driver.find_element_by_id("new-project_project_description")
    name_decsription.send_keys(messageDecsription)
    driver.find_element_by_class_name('ant-btn-primary').click()
    return driver


#操作项目-进入章节
#第一章
def operationProjectGropup(driver):
    time.sleep(0.5)
    chapter_one = driver.find_elements_by_tag_name("tr")[-1]
    chapter_one.click()
    return driver

#上传资源
def upload(driver):
    time.sleep(0.5)
    upload_click = driver.find_elements_by_tag_name("li")[5]
    upload_click.click()
    return driver

#上传图片等  支持扩展名：mp3、mp4、gif、jpg、png、xls、xlsx、json
def uploadPhoto(driver):
    time.sleep(0.5)

    list_name = os.listdir(file_path+r"/resources")
    file_path_local = file_path + '/resources/'
    # print(list_name)
    for x in list_name:
        # print(file_path_local+x)
        upload_photo = driver.find_elements_by_tag_name('input')[0]
        a = upload_photo.send_keys(file_path_local+x)
        # print('111111',a)
    time.sleep(10)
    return driver



#数值操作
def opertionNum(driver):
    time.sleep(0.5)
    make_num = driver.find_elements_by_tag_name("li")[6]
    make_num.click()
    #添加数值
    l = [
            {
            'editor-var_alias': '选择结果字符串3',
            'editor-var_name': 'resultString3',
            'editor-var_type': '字符',
            'editor-var_sVal': 'a',
            'editor-var_scope': '本地'
            },
            {
                'editor-var_alias': '选择结果1',
                'editor-var_name': 'result1',
                'editor-var_nVal': '0',
                'editor-var_type': '数值',
                'editor-var_scope': '本地'
            },
        ]
    for k in l:
        time.sleep(a)
        add_num_click = driver.find_elements_by_class_name('ant-page-header-heading-extra')[1]
        add_num_click.click()
        print(k)
        for x,y in k.items():
            time.sleep(a)
            # print(x,y)
            if x not in ['editor-var_type','editor-var_scope']:
                driver.find_element_by_id(x).send_keys(y)

            if y == "字符":
                # driver.find_element_by_id(x).send_keys(y)
                driver.find_element_by_id(x).click()
                string = (driver.find_elements_by_tag_name('ul')[-1]).find_elements_by_tag_name('li')[1]
                string.click()
            elif y == '数值':
                # num_input = driver.find_element_by_class_name('ant-input-number-input')
                # num_input.send_keys()
                pass
                # driver.find_element_by_id(x).click()
                # string = (driver.find_elements_by_tag_name('ul')[-1]).find_elements_by_tag_name('li')[0]
                # string.click()
            if x == 'editor-var_scope':
                driver.find_element_by_id(x).click()
                string = (driver.find_elements_by_tag_name('ul')[-1]).find_elements_by_tag_name('li')[1]
                string.click()
        driver.find_elements_by_class_name('ant-btn-primary')[1].click()
    return driver


def end(driver):
    time.sleep(5)
    driver.execute_script('alert("测试完成")')
    time.sleep(15)
    driver.quit()
    return


if __name__ == "__main__":

    a = 3
    driver = login()
    # 隐式等待
    driver.implicity_wait(10)
    time.sleep(a)
    driver = clickSearch(driver)
    time.sleep(a)
    driver = goProjectGroup(driver)
    time.sleep(a)
    driver = makeProjectGroup(driver,'11','11','5')
    time.sleep(a)
    driver = operationProjectGropup(driver)
    time.sleep(a)
    driver = upload(driver)
    time.sleep(a)
    driver = uploadPhoto(driver)
    time.sleep(a)
    driver = opertionNum(driver)
    time.sleep(a)
    end(driver)



