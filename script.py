from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import requests
import time
import logging
import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from time import sleep
import re
import csv
from selenium.common.exceptions import NoSuchElementException

#logging.basicConfig(level=logging.DEBUG)

class Scraper():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        #options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        chrome_path = '/usr/local/bin/chromedriver'
        #chrome_path = 'C:/chromedriver/chromedriver.exe'
        #self.base_url = 'https://auktion.kronofogden.se/'
        self.driver = webdriver.Chrome(chrome_path,options=options)

    district = {
        'Alabama': 10,
        '*Alaska': 0,
        'American Samoa': 0,
        'Arizona': 9,
        'Arkansas': 7,
        'California': 53,
        'Colorado': 7,
        'Connecticut': 6,
        '*Delaware': 0,
        'District of Columbia': 0,
        'Florida': 27,
        'Georgia': 14,
        'Guam': 0,
        'Hawaii': 2,
        'Idaho': 2,
        'Illinois': 26,
        'Indiana': 13,
        'Iowa': 11,
        'Kansas': 8,
        'Kentucky': 13,
        'Louisiana': 8,
        'Maine': 8,
        'Maryland': 8,
        'Massachusetts': 20,
        'Michigan': 19,
        'Minnesota': 10,
        'Mississippi': 8,
        'Missouri': 16,
        'Montana': 2,
        'Nebraska': 6,
        'Nevada': 4,
        'New Hampshire': 4,
        'New Jersey': 15,
        'New Mexico': 3,
        'New York': 45,
        'North Carolina': 13,
        'North Dakota': 3,
        'Northern Mariana Islands': 0,
        'Ohio': 24,
        'Oklahoma': 8,
        'Oregon': 5,
        'Pennsylvania': 36,
        'Philippines': 0,
        'Puerto Rico': 0,
        'Rhode Island': 3,
        }
        
    # district_list = []
    # for i in district.values():
    #     print(i)



    def format_company(self, url):
        url = self.driver.get(url)
        #profile_last_updated_date =  self.driver.find_element_by_xpath("//*[contains(text(), 'This profile was last updated:')]")

        """
            IDENTIFICATION, LOCATION AND CONTACTS
        """
        profile_last_updated_date = datetime.datetime.strptime((self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[1]/div[2]")).text, '%m-%d-%Y')
        print("LAST DATE", profile_last_updated_date)
        status =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[2]/div[2]")
        print("STATUS", status.text)
        user_id =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[3]/div[2]")
        print("USER ID",  user_id.text)
        name_of_firm =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[4]/div[2]")
        print("NAME OF FIRM", name_of_firm.text)
        duns_number =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[6]/div[2]")
        print("DUNS NUMBER", duns_number.text)
        address_line_1 =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[8]/div[2]")
        print("ADDRESS LINE 1", address_line_1.text)
        address_line_2 =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[9]/div[2]")
        print("ADDRESS LINE 2", address_line_2.text)
        city =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[10]/div[2]")
        print("CITY", city.text)
        state =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[11]/div[2]")
        print("STATE", state.text)
        zip =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[12]/div[2]")
        print("ZIP", zip.text)
        phone_no =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[13]/div[2]")
        print("PHONE", phone_no.text)
        try:
            fax_no =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[14]/div[2]")
            print("FAX", fax_no.text)
        except:
           print("FAX", "N/A")
        email =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[15]/div[2]")
        print("EMAIL", email.text)
        www =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[16]/div[2]")
        print("WWW", www.text)
        ecommerce_website =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[17]/div[2]")
        print("E-Commerce", ecommerce_website.text)
        contact_person =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[18]/div[2]")
        print("Contact person", contact_person.text)
        county_code =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[19]/div[2]")
        print("County code", county_code.text)
        congressional_district =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[20]/div[2]")
        print("congressional district", congressional_district.text)
        metropolitan_statistical_area =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[21]/div[2]")
        print("metropolitan statistical area", metropolitan_statistical_area.text)
        cage_code =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[22]/div[2]")
        print("cage code", cage_code.text)
        year_established =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[23]/div[2]")
        year_established = datetime.datetime.strptime(year_established.text, '%Y')
        print("year established", year_established)
        accepts_govt_credit_card =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[2]/div/div/div[24]/div[2]")
        if accepts_govt_credit_card.text == "[  ] Yes [X] No":
            accepts_govt_credit_card = False
        elif accepts_govt_credit_card.text == "[X] Yes [  ] No":
            accepts_govt_credit_card = True
        legal_structure =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[1]/div[2]")
        print("legal structure", legal_structure.text)
        ownership_and_self_certifications =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[2]/div[2]")
        print("ownership and self certifications", ownership_and_self_certifications.text)
        current_principals =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[3]")
        if current_principals.text == "(none given)":
            current_principals = ""
        else:
            current_principals = current_principals.text
        print("current principals", current_principals)
        business_development_servicing_office = self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[3]/div/div[4]')
        print("business development servicing office", business_development_servicing_office.text)
        """
            SBA FEDERAL CERTIFICATIONS
        """           
        eight_a_case_number =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[6]/div[2]")
        print("8(a) case number", eight_a_case_number.text)
        eight_b_entrance_date =  (self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[7]/div[2]")).text
        try:
            eight_b_entrance_date = datetime.datetime.strptime(eight_b_entrance_date.text, '%Y-%m-%d')
        except:
            pass
        print("8(b) entrance date", eight_b_entrance_date)
        eight_c_exit_date =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[8]/div[2]")
        try:
            eight_c_exit_date = datetime.datetime.strptime(eight_c_exit_date.text, '%Y-%m-%d')
        except:
            pass
        print("8(c) exit date", eight_c_exit_date)
        is_hubzone_certified =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[9]/div[2]")
        if is_hubzone_certified.text == "[  ] Yes [X] No":
            is_hubzone_certified = False
        elif is_hubzone_certified.text == "[X] Yes [  ] No":
            is_hubzone_certified = True
        else:
            is_hubzone_certified = ""
        print("is hubzone certified?", is_hubzone_certified)
        # hubzone_certified_date =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[10]/div[2]")
        # print("hubzone certified date", hubzone_certified_date.text)

        jv_entrance_date =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[11]/div[2]")
        try:
            jv_entrance_date = datetime.datetime.strptime(jv_entrance_date.text, '%m-%d-%Y')
        except:
            jv_entrance_date = ""
        print("jv entrance date", jv_entrance_date)
        jv_exit_date =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[12]/div[2]")
        try:
            jv_exit_date = datetime.datetime.strptime(jv_exit_date.text, '%m-%d-%Y')
        except:
            jv_exit_date = ""
        print("jv exit date", jv_exit_date)

        is_wosb_certified =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[13]/div[2]")
        if is_wosb_certified.text == "[  ] Yes [X] No":
            is_wosb_certified = False
        elif is_wosb_certified.text == "[X] Yes [  ] No":
            is_wosb_certified = True
        else:
            is_wosb_certified = ""
        print("is wosb certified?", is_wosb_certified)
        # wosb_certification_date =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[14]/div[2]")
        # print("wosb certification date", wosb_certification_date.text)

        is_edwosb_certified =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[15]/div[2]")
        if is_edwosb_certified.text == "[  ] Yes [X] No":
            is_edwosb_certified = False
        elif is_edwosb_certified.text == "[X] Yes [  ] No":
            is_edwosb_certified = True
        else:
            is_edwosb_certified = ""
        print("is edwosb certified?", is_edwosb_certified)
        # edwosb_certification_date =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[16]/div[2]")
        # print("edwosb certification date", edwosb_certification_date.text)
        """
            OTHER CERTIFICATIONS
        """  
        non_federal_government_certifications = self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[3]/div/div[18]")
        if non_federal_government_certifications.text == "(none given)":
            non_federal_government_certifications = ""
        elif non_federal_government_certifications.text == "EDWOSB Pending?: [X] Yes [  ] No":
            non_federal_government_certifications = "EDWOSB Pending"            
        else:
            non_federal_government_certifications = non_federal_government_certifications.text
        print("non federal government certifications", non_federal_government_certifications)
        """
            PRODUCTS & SERVICES
        """  
        capabilities_narrative =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[4]/div/div[1]")
        if capabilities_narrative.text == "(none given)":
            capabilities_narrative = ""
        else:
            capabilities_narrative = capabilities_narrative.text
        print("capabilities narrative", capabilities_narrative)
        special_equipment_materials =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[4]/div/div[2]")
        if special_equipment_materials.text == "(none given)":
            special_equipment_materials = ""
        else:
            special_equipment_materials = special_equipment_materials.text
        print("special equipment materials", special_equipment_materials)
        business_type_percentages =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[4]/div/div[3]")
        if business_type_percentages.text == "(none given)":
            business_type_percentages = ""
        else:
            business_type_percentages = business_type_percentages.text
        print("business type percentages", business_type_percentages)

        construction_bonding_level_per_contract =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[4]/div/div[4]/div[2]")
        if construction_bonding_level_per_contract.text == "(none given)":
            construction_bonding_level_per_contract = ""
        else:
            construction_bonding_level_per_contract = construction_bonding_level_per_contract.text
        print("construction bonding level per contract", construction_bonding_level_per_contract)
        construction_bonding_level_aggregate =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[4]/div/div[5]/div[2]')
        if construction_bonding_level_aggregate.text == "(none given)":
            construction_bonding_level_aggregate = ""
        else:
            construction_bonding_level_aggregate = construction_bonding_level_aggregate.text
        print("construction bonding level aggregate", construction_bonding_level_aggregate)
        service_bonding_level_per_contract =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[4]/div/div[6]/div[2]")
        if service_bonding_level_per_contract.text == "(none given)":
            service_bonding_level_per_contract = ""
        else:
            service_bonding_level_per_contract = service_bonding_level_per_contract.text
        print("service bonding level per contract", service_bonding_level_per_contract)
        service_bonding_level_aggregate =  self.driver.find_element_by_xpath("//*[@id='DivAppData']/div/div[4]/div/div[7]/div[2]")
        if service_bonding_level_aggregate.text == "(none given)":
            service_bonding_level_aggregate = ""
        else:
            service_bonding_level_aggregate = service_bonding_level_aggregate.text
        print("service bonding level aggregate", service_bonding_level_aggregate)
        """
            NAICS CODES WITH SIZE DETERMINATIONS BY NAICS
        """ 
        try:
            primary_code =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[4]/div/div[8]/table/tbody/tr[1]/td[3]')
            print("primary code", primary_code.text)
        except:
            primary_code = ""
        try:
            primary_description =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[4]/div/div[8]/table/tbody/tr[1]/td[4]')
            print("primary description", primary_description.text)
        except:
            primary_description = ""
        


        the_list = []
        time.sleep(10)
        tbody = self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[4]/div/div[8]/table/tbody')
        no_of_secondary = tbody.find_elements_by_xpath(".//tr")
        for i in range(2, len(no_of_secondary) + 1):
            path = '//*[@id="DivAppData"]/div/div[4]/div/div[8]/table/tbody/tr[' + str(i) + ']/td[3]'
            code = self.driver.find_element_by_xpath(path)
            the_list.append(code.text)

        if the_list == []:
            the_list = ""
        val = {"primary": {"code": primary_code.text, "description": primary_description.text}, "secondary": the_list}
        print("SECONDARY", val)

        good_keywords =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[4]/div/div[9]')
        if good_keywords.text == "(none given)":
            good_keywords = ""
        else:
            good_keywords = good_keywords.text
        print("good_keywords", good_keywords)

        quality_assurance_standards =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[4]/div/div[10]/div[2]')
        if quality_assurance_standards.text == "(none given)":
            quality_assurance_standards = ""
        else:
            quality_assurance_standards = quality_assurance_standards.text
        print("quality assurance standards", quality_assurance_standards)
        is_electronic_data_interchange_capable =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[4]/div/div[11]/div[2]')
        if is_electronic_data_interchange_capable.text == "[  ] Yes [X] No":
            is_electronic_data_interchange_capable = False
        elif is_electronic_data_interchange_capable.text == "[X] Yes [  ] No":
            is_electronic_data_interchange_capable = True
        else:
            is_electronic_data_interchange_capable = ""
        print("is electronic data interchange capable?", is_electronic_data_interchange_capable)
        """
            EXPORT PROFILE (TRADE MISSION ONLINE)
        """  
        is_exporter =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[5]/div/div[1]/div[2]')
        if is_exporter.text == "(firm hasn't answered this question yet)" or is_exporter.text == "(none given)": 
            is_exporter = ""
        elif is_exporter.text == "[  ] Yes [X] No [  ] Wants To Be":
            is_exporter = False
        elif is_exporter.text == "[X] Yes [  ] No [  ] Wants To Be":
            is_exporter = True
        else:
            is_exporter = ""            
        print("is exporter", is_exporter)
        export_business_activities =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[5]/div/div[2]/div[2]')
        if export_business_activities.text == "(none given)":
            export_business_activities = ""
        else:
            export_business_activities = export_business_activities.text
        print("export business activities", export_business_activities)
        exporting_to =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[5]/div/div[3]/div[2]')
        if exporting_to.text == "(none given)":
            exporting_to = ""
        else:
            exporting_to = exporting_to.text
        print("exporting to", exporting_to)
        desired_export_business_relationships =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[5]/div/div[4]/div[2]')
        if desired_export_business_relationships.text == "(none given)":
            desired_export_business_relationships = ""
        else:
            desired_export_business_relationships = desired_export_business_relationships.text
        print("desired export business relationships", desired_export_business_relationships)
        description_of_export_objectives =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[5]/div/div[5]/div[2]')
        if description_of_export_objectives.text == "(none given)":
            description_of_export_objectives = ""
        else:
            description_of_export_objectives = description_of_export_objectives.text
        print("description of export objectives", description_of_export_objectives)
        """
            PERFORMANCE HISTORY (REFERENCES)
        """          
        performance_history_references =  self.driver.find_element_by_xpath('//*[@id="DivAppData"]/div/div[6]/div/div')
        if performance_history_references.text == "(none given)":
            performance_history_references = ""
        else:
            performance_history_references = performance_history_references.text
        print("performance history references", performance_history_references)

        output_dict = ({"_id": int(user_id.text), "profilesubmissiondate": profile_last_updated_date, "status": status.text, 
            "companylegalname": name_of_firm.text, "dunsnumber": duns_number.text, "addressline1": address_line_1.text, 
            "addressline2": address_line_2.text, "city": city.text, "state": state.text, "zip": zip.text,
            "streetaddress": address_line_1.text + ',' + address_line_2.text + city.text + ',' + state.text + ',' + zip.text, 
            "phonenumber": phone_no.text,"fax": fax_no.text, "emailaddress": email.text, "businesswebsite": www.text, 
            "e-commerce_website": ecommerce_website.text, "contact_person": contact_person.text,
            "county_code": county_code.text, "congressionaldistrict": congressional_district.text,
            "metropolitan_statistical_area": metropolitan_statistical_area.text, "cagecode": cage_code.text, 
            "businessstartdate": year_established, "accepts_govt_credit_card": accepts_govt_credit_card,
            "gsa_advantage_contract": gsa_advantage_contract.text, "legal_structure": legal_structure.text, 
            "ownership_and_self_certifications": ownership_and_self_certifications.text, 
            "current_principals": current_principals, 
            "business_development_servicing_office": business_development_servicing_office.text, 
            "8(a)_case_number": eight_a_case_number.text, "8(b)_entrance_date": eight_b_entrance_date,
            "8(c)_exit_date": eight_c_exit_date.text, "is_hubzone_certified": is_hubzone_certified, 
            "jv entrance date": jv_entrance_date, "jv_exit_date": jv_exit_date, 
            "is_wosb_certified": is_wosb_certified, "is_edwosb_certified": is_edwosb_certified,
            "non_federal_government_certifications": non_federal_government_certifications,
            "companydescription": capabilities_narrative, 
            "special_equipment_materials": special_equipment_materials,
            "business_type_percentages": business_type_percentages,
            "construction_bonding_level_per_contract": construction_bonding_level_per_contract,
            "construction_bonding_level_aggregate": construction_bonding_level_aggregate,
            "service_bonding_level_per_contract": service_bonding_level_per_contract,
            "service_bonding_level_aggregate": service_bonding_level_aggregate,
            "primarynaicscode": primary_code.text, "primarynaicscodedescription": primary_description.text, "additionalnaicscodes": the_list, 
            "good_keywords": good_keywords, "quality_assurance_standards": quality_assurance_standards, 
            "is_electronic_data_interchange_capable": is_electronic_data_interchange_capable,
            "is_exporter": is_exporter, "specialtiesexported": export_business_activities, 
            "exporting_to": exporting_to, "desired_export_business_relationships":desired_export_business_relationships,
            "description_of_export_objectives": description_of_export_objectives,
            "performance_history_references": performance_history_references
            })
        # print("TYPE", type(output_dict))
        return output_dict


    def act(self):
        url = self.driver.get("https://web.sba.gov/dsbs/search/dsp_dsbs.cfm")

        selected_state = self.driver.find_element_by_xpath("//*[@id='EltState']/option[2]")
        selected_state.click()
        time.sleep(2)
        district_box = self.driver.find_element_by_id("EltCdist")
        district_box.send_keys('01')
        time.sleep(2)
        search_button = self.driver.find_element_by_xpath("//*[@id='DivAppData']/form/div[2]/input[1]")
        search_button.click()

        tbody = self.driver.find_element_by_tag_name("tbody")
        company_link = []
        for i in range(10):
            next_button = self.driver.find_element_by_xpath("//*[@id='PagingOptions']/input[1]")
            qq = self.driver.find_elements_by_xpath("//td[2]/a")
            rr =  [each.get_attribute('href') for each in qq if each.get_attribute('href').startswith("http")]
            print("WWWWWWWW", len(qq))
            company_link.extend(rr)
            next_button.click()
        print("Finished", len(company_link))
        #//*[@id="ProfileTable"]/tbody/tr[1]/td[2]
        # company_link = []
        # next_button_list = self.driver.find_elements_by_xpath('//*[@id="PagingOptions"]/table/tbody/tr[3]/td[10]/a[1]')
        # pages = 0
        # print("NUMBER OF NEXT BUTTON", next_button_list)
        # while len(next_button_list) > 0:
        #     time.sleep(5)
        #     # qq = tbody.find_elements_by_xpath("//td[2]/a")
        #     qq = self.driver.find_elements_by_xpath("/html/body/div[2]/div[5]/div[4]/div/div/div[2]/center/table/tbody/tr[1]/td[2]/a")
        #     pages += 1
        #     print(pages, len(qq))
        #     company_link.append(qq)
        #     next_button_list[0].send_keys(Keys.PAGE_DOWN)
        #     time.sleep(4)
        #     if pages == 1:
        #         next_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[4]/div/div/form/div/div[1]/table/tbody/tr[3]/td[10]/a[1]')
        #     else:
        #         next_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[5]/div[4]/div/div/form/div/div[1]/table/tbody/tr[3]/td[11]/a[1]')
        #     next_button.click()
        # company_link = [each.get_attribute('href') for each in company_link if each.get_attribute('href').startswith("http")]
        # print("COMPANY LINKS", company_link, len(company_link))
        # return "Finished"
        time.sleep(6)
        #company_link = tbody.find_elements_by_xpath("//td[2]/a")
        print("CCL", len(company_link), company_link[0:2])



        out = []
        for each_link in company_link:
            single_url = self.format_company(each_link)
            out.append(single_url)
            time.sleep(2)



        field_names = [ "_id", "profilesubmissiondate", "status", "companylegalname", "dunsnumber", "addressline1", "addressline2", 
            "city", "state", "zip", "streetaddress", "phonenumber", "fax", "emailaddress", "businesswebsite", "e-commerce_website", "contact_person", "county_code", 
            "congressionaldistrict", "metropolitan_statistical_area", "cagecode", "businessstartdate", "accepts_govt_credit_card",
            "gsa_advantage_contract", "legal_structure", "ownership_and_self_certifications", "current_principals", 
            "business_development_servicing_office", "8(a)_case_number", "8(b)_entrance_date", "8(c)_exit_date", "is_hubzone_certified",
            "jv entrance date", "jv_exit_date", "is_wosb_certified", "is_edwosb_certified", "non_federal_government_certifications", 
            "companydescription", "special_equipment_materials", "business_type_percentages", "construction_bonding_level_per_contract",
            "construction_bonding_level_aggregate", "service_bonding_level_per_contract", "service_bonding_level_aggregate",
            "primarynaicscode", "primarynaicscodedescription", "additionalnaicscodes", "good_keywords", "quality_assurance_standards", 
            "is_electronic_data_interchange_capable", "is_exporter", "specialtiesexported", "exporting_to",
            "desired_export_business_relationships", "description_of_export_objectives", "performance_history_references"]

        csv_file = "output.csv"
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=field_names)
                writer.writeheader()
                for data in out:
                    writer.writerow(data)
        except IOError:
            print("I/O error")

        return True

        #return out


    #     all_results = []
    #     num_of_twos = 0
    #     page = 1
    #     while True:
    #         table = self.driver.find_elements_by_xpath("//*[@class='obj_thumbnail img-thumbnail']")
    #         print("NOW IN PAGE", page)
    #         print("LEN OF TABLE", len(table))
    #         for tabl in table:
    #             id = tabl.get_attribute('id')
    #             image_url = tabl.find_element_by_tag_name('img').get_attribute('src')
    #             time.sleep(3)
    #             params = tabl.find_element_by_css_selector('div[class=obj_txt_inner]').text.splitlines()
    #             title = params[0]
    #             splited_title = title.split()
    #             title = ' '.join(splited_title[1:])
    #             location = params[1]
    #             estimate = params[2]
    #             splited_estimate = estimate.split()
    #             estimate = ' '.join(splited_estimate[1:])
    #             link = tabl.find_element_by_tag_name('a').get_attribute('href')
    #             time.sleep(5)
    #             time_remaining = tabl.find_elements_by_xpath('//*[@id=' + str(id) + ']/div[1]/span[2]')[0].get_attribute('textContent')
    #             try: 
    #                 highest_bid = tabl.find_element_by_xpath('//*[@id=' + str(id) + ']/div[3]/a/div[4]/div/span[3]/span[1]').text
    #                 splited_highest_bid = highest_bid.split()
    #                 highest_bid = ' '.join(splited_highest_bid[2:])
    #             except:
    #                 highest_bid = None
    #             result = {"title":title,"location":location,"estimate":estimate,"item_url":link,"time_remaining":time_remaining,"highest_bid":highest_bid, "image_url":image_url}
    #             all_results.append(result)
    #         no_disabled = self.driver.find_element_by_xpath('/html/body/div[1]/div[9]/div[1]/div/ul')
    #         no_disabled = no_disabled.find_elements_by_css_selector('li[class=disabled]')
    #         time.sleep(2)
    #         pre_next_button = self.driver.find_element_by_xpath("/html/body/div[1]/div[9]/div[1]/div/ul")
    #         next_button = pre_next_button.find_elements_by_tag_name('li')[-2]
    #         next_button = next_button.find_element_by_tag_name('a')
    #         time.sleep(3)
    #         if len(no_disabled) == 2:
    #             num_of_twos += 1
    #         if num_of_twos == 2:
    #             break
    #         print("NEXT BUTTON", next_button)
    #         next_button.click()
    #         page += 1


s = Scraper()
s.act()
#print(s)