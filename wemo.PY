import flet as ft

def main(page: ft.Page):
    
       
    page.title = "WEMO "
    page.theme = ft.Theme(font_family="Kanit")
    page.theme_mode=ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.auto_scroll = False
    page.scroll = ft.ScrollMode.HIDDEN
    page.padding = 10
    
    def ThemeMode_LIGHT (_):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.update()
        
    def ThemeMode_DARK  (_):   
         page.theme_mode = ft.ThemeMode.DARK
         page.update()


    def on_hover(e):
        e.control.bgcolor = "BLUE_900" if e.data == "true" else "BLUE"
        e.control.update()


    def open_url(e):
        page.launch_url(e.data)


    def on_click1(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Sorry your answer is wrong, try again!"))
        page.snack_bar.open = True
        page.update()

    def on_click2(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"Conglatulation your answer is right!"))
        page.snack_bar.open = True
        page.update()


    


    def check_item_clicked(e):
        e.control.checked = not e.control.checked
        page.update()













    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.AppBar(
       
        toolbar_height=90,
        bgcolor=ft.colors.BLUE_900,
        title=ft.Row([
            ft.Container(
            padding=ft.padding.all(4),
            border=ft.border.all(3,"white"),
            border_radius=ft.border_radius.all(30),
            content=ft.Text("WEMO",color="white",size=30)
            ),
        
             ]),
        

            
    
        center_title=False,
          actions=[ ft.TextButton("MENU",icon_color="white", on_click=lambda _: page.go("/menu"),icon=ft.icons.INFO_OUTLINE_SHARP),
            ft.TextButton("Quiz", icon_color="white",on_click=lambda _: page.go("/quiz"),icon=ft.icons.QUIZ,),
          ],
        
    ),







                    



                    ft.Image(src="c1.png",border_radius=30,fit=ft.ImageFit.COVER,),
                               
                  



                    
                  ft.Text("COURSES",weight=ft.FontWeight.BOLD, color="white",style=ft.TextThemeStyle.HEADLINE_MEDIUM),
    

                   ft.Container(
                    content=ft.Text("Choose a course to start learning with us on WEMO",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                     shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                    
                ),  
    
    







                    ft.Text("COMPUTER SCIENCE",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("JAVA         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                   ft.Text("Learning Java opens up your possibilities when coding. With it, you'll be able to develop large systems, software, and mobile applications — and even create mobile apps for Android.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                ft.Markdown(
            "[JAVA](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("DATABASE CONCEPTS AND TECHNOLOGY        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                     ft.Text("Study the principles of designing, implementing, and managing databases for storing and retrieving data.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[DATABASE CONCEPTS AND TECHNOLOGY](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("OPEN SOURCE OPERATING SYSTEM         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn about the design and functionalities of operating systems that manage computer hardware and software resources.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[OPEN SOURCE OPERATING SYSTEM](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("VISUAL STUDIO         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Visual Studio Code is a code editor redefined and optimized for building and debugging modern web and cloud applications.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.Markdown(
            "[VISUAL STUDIO](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("MOBILE APP         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Learn how to create mobile applications for Android or iOS platforms.     ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[MOBILE APP](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("WEB BASED CONCEPTS AND DEVL.         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Learn how to create dynamic websites and web applications using HTML, CSS, JavaScript, and web frameworks.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[WEB BASED CONCEPTS AND DEVL.](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    




                      ft.Container(
                    content=ft.Column([ft.Text("SURVEY OF PROGRAMMING LANG.           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("The primary goal would be to introduce students to a variety of programming languages, their features, and use cases.        ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[SURVEY OF PROGRAMMING LANG.](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("DATA STRUCTURES I         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study different data structures (e.g., arrays, linked lists, trees) and algorithms (e.g., searching, sorting) used to solve computational problems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[DATA STRUCTURES I](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("OPERATION RESEARCH I        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("A branch of mathematics that uses various mathematical, statistical, and computational techniques to optimize and improve decision-making processes.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[OPERATION RESEARCH I](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("DATA STRUCTURES II        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text(" Study different data structures (e.g., arrays, linked lists, trees) and algorithms (e.g., searching, sorting) used to solve computational problems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    
        ft.Markdown(
            "[DATA STRUCTURES II](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("OPERATION RESEARCH II         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("A branch of mathematics that uses various mathematical, statistical, and computational techniques to optimize and improve decision-making processes.              ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[OPERATION RESEARCH II ](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    

 ft.Divider(),



 ft.Text("NATURAL RESOURSES",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Soil and Water Resources Management         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text(" Focus on the conservation and sustainable use of soil and water resources in agricultural and natural ecosystems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                ft.Markdown(
            "[Soil and Water Resources Management](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Renewable Energy and Sustainability        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                     ft.Text(" Explore alternative energy sources and sustainable practices to reduce environmental impacts.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Renewable Energy and Sustainability](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Natural Resource Economics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study the economic principles and valuation of natural resources and their impact on decision-making.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Natural Resource Economics](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                 height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Environmental Policy and Law         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Examine the legal and policy frameworks that govern natural resources management at local, national, and international levels.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   ft.Markdown(
            "[Environmental Policy and Law](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                 height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Geographic Information Systems (GIS) and Remote Sensing         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Gain skills in using geospatial technologies to analyze and visualize natural resource data.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Geographic Information Systems (GIS) and Remote Sensing](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Sustainable Resource Management        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn about strategies for sustainable use and management of natural resources, including forests, water, wildlife, and minerals.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Sustainable Resource Management](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
             height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Conservation Biology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Explore principles and practices for conserving biodiversity and natural ecosystems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Conservation Biology](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Environmental Science           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Study the interactions between living organisms and their environment, including topics such as ecology, environmental pollution, and climate change.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Environmental Science](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Environmental Data Analysis         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Learn statistical and analytical methods for interpreting and analyzing environmental data.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Environmental Data Analysis](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Environmental Ethics        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Examine ethical issues and responsibilities related to natural resource use and conservation.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[Environmental Ethics](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                 height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Indigenous Knowledge and Resource Management        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Explore the role of indigenous communities in natural resource management and conservation.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    
        ft.Markdown(
            "[Indigenous Knowledge and Resource Management](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
             height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Sustainable Development         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study the principles of sustainable development and how they relate to natural resource management.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[Sustainable Development](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
             height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    


      
 ft.Divider(),


        
              
 ft.Text("OPTOMETRY",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Anatomy and Physiology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
               ft.Text("Study the structure and function of the human body, with a specific focus on the anatomy and physiology of the eye and visual system.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                ft.Markdown(
            "[Anatomy and Physiology](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Ocular Biology        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Explore the biology and histology of the eye, including the cornea, lens, retina, and other ocular structures.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Ocular Biology](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Optics and Refraction         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Learn about the principles of light, optics, and the process of refraction for correcting vision problems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Optics and Refraction](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                 height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Visual Optics        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study how light interacts with the eye's optical components and how eyeglasses and contact lenses correct vision.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   ft.Markdown(
            "[Visual Optics](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                 height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Ocular Disease and Pathology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Examine various eye diseases, conditions, and pathologies, including glaucoma, cataracts, and retinal disorders.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Ocular Disease and Pathology](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Binocular Vision and Vision Therapy         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore how the eyes work together and how to diagnose and treat binocular vision problems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Binocular Vision and Vision Therapy](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
             height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Pharmacology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn about ocular pharmacology, including the use of drugs and medications in eye care.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Pharmacology](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Pediatric Optometry           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Focus on vision care for children, including pediatric eye exams and vision development.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Pediatric Optometry](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Geriatric Optometry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study the unique vision and eye care needs of older adults.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Geriatric Optometry](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                     height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Low Vision Rehabilitation        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn techniques and devices to help individuals with low vision maximize their remaining sight.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[Low Vision Rehabilitation](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                 height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Contact Lens Fitting and Management        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    
                    ft.Text("Gain knowledge and skills in fitting and managing contact lenses for patients.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


        ft.Markdown(
            "[Contact Lens Fitting and Management](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
             height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Clinical Optometry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Participate in supervised clinical rotations to gain practical experience in diagnosing and managing eye conditions.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[Clinical Optometry](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
             height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    

             


 ft.Divider(),





 ft.Text("PHYSICS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Classical Mechanics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text(" Study the laws of motion and how they govern the behavior of macroscopic objects.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                ft.Markdown(
            "[Classical Mechanics](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Electromagnetism        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                     ft.Text("Explore the principles of electricity and magnetism, including Maxwell's equations.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Electromagnetism](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Quantum Mechanics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn about the principles of quantum theory, wave-particle duality, and the behavior of subatomic particles.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Quantum Mechanics](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Thermodynamics and Statistical Mechanics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study the concepts of heat, work, and entropy, as well as statistical approaches to understanding the behavior of systems with a large number of particles.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   ft.Markdown(
            "[Thermodynamics and Statistical Mechanics](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Optics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Explore the behavior of light and its interactions with matter.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Optics](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Modern Physics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Cover topics such as special relativity and the basics of atomic and nuclear physics.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Modern Physics](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Solid State Physics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Focus on the properties of solid materials and their behavior using quantum mechanics.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Solid State Physics](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Fluid Mechanics           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study the behavior of fluids, including liquids and gases, and the principles of fluid dynamics.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Fluid Mechanics](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Astrophysics and Cosmology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore the physics of celestial objects and the origin and evolution of the universe.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Astrophysics and Cosmology](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Computational Physics       ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Learn how to use computational methods to solve complex physics problems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[Computational Physics](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,











           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    

 

     
 ft.Divider(),






 ft.Text("MATHEMATICS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Introduction to Mathematics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("A foundational course that provides an overview of basic mathematical concepts and principles.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                ft.Markdown(
            "[Introduction to Mathematics](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Calculus        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Courses in calculus cover differential and integral calculus, which are fundamental to understanding change and accumulation in mathematics.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Calculus](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Linear Algebra         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore the algebraic structures of vector spaces and linear transformations, essential for various applications in science and engineering.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Linear Algebra](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Discrete Mathematics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Focuses on discrete structures like sets, graphs, and combinatorics, which have applications in computer science and cryptography.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   ft.Markdown(
            "[Discrete Mathematics](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Probability and Statistics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Learn about probability theory and statistical methods used for data analysis and decision-making.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Probability and Statistics](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Number Theory         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Dive into the properties and relationships of integers, including prime numbers and modular arithmetic.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Number Theory](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Differential Equations         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study ordinary and partial differential equations, which are crucial for modeling dynamic systems in physics, engineering, and other fields.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Differential Equations](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Real Analysis           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("An in-depth study of the rigorous foundations of calculus and the properties of real numbers and functions.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                     ft.Markdown(
            "[Real Analysis](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Abstract Algebra         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Explore algebraic structures like groups, rings, and fields, which have applications in cryptography and coding theory.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    ft.Markdown(
            "[Abstract Algebra](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Topology        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Investigate the properties of spaces and their continuous transformations, with applications in geometry and topology.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[Topology](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Mathematical Logic        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text(" Study the principles and methods of mathematical reasoning and proof.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                    
        ft.Markdown(
            "[Mathematical Logic](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Mathematical Modeling         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn how to use mathematics to model and analyze real-world problems in various fields.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),


                   
        ft.Markdown(
            "[Mathematical Modeling](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    







 ft.Divider(),







 ft.Text("CHEMISTRY",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("General Chemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("A foundational course that introduces the basic principles of chemistry, including atomic structure, chemical bonding, stoichiometry, and gas laws.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                ft.Markdown(
            "[General Chemistry](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Organic Chemistry        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                     ft.Text("Focuses on the study of carbon compounds and reactions, essential for understanding biochemistry and many industrial processes.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Organic Chemistry](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Inorganic Chemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explores the chemistry of inorganic compounds and elements, including transition metals and coordination complexes.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Inorganic Chemistry](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Physical Chemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Combines principles of physics and chemistry to study the physical properties and behavior of chemical systems.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.Markdown(
            "[Physical Chemistry](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Analytical Chemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Teaches various techniques for analyzing and characterizing chemical substances and determining their composition.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Analytical Chemistry](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Biochemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Examines the chemical processes within living organisms, with a focus on biomolecules and their functions.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Biochemistry](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Environmental Chemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explores the impact of chemical processes on the environment, including pollution and climate change.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Environmental Chemistry](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Computational Chemistry           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Introduces computational methods used to study chemical systems and predict their properties.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Computational Chemistry](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Medicinal Chemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Focuses on the design and synthesis of pharmaceutical compounds and their interaction with biological targets.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Medicinal Chemistry](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Materials Chemistry        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Studies the properties, synthesis, and applications of different materials, such as polymers, ceramics, and nanomaterials.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Materials Chemistry](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Quantum Chemistry        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text(" Explores the application of quantum mechanics to understand the behavior of atoms and molecules.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    
        ft.Markdown(
            "[Quantum Chemistry](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Chemical Engineering         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Integrates principles of chemistry and engineering to design and optimize chemical processes and manufacturing.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Chemical Engineering ](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    




        

 ft.Divider(),








 ft.Text("STATISTICS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Introduction to Statistics        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("A foundational course that provides an overview of basic statistical concepts, including data types, descriptive statistics, and probability.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                ft.Markdown(
            "[Introduction to Statistics](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Statistical Inference        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                     ft.Text("This course focuses on methods for drawing conclusions and making predictions from data, including hypothesis testing and confidence intervals.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Statistical Inference](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Regression Analysis        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text(" Learn about linear regression and its applications in modeling relationships between variables.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Regression Analysis](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Multivariate Statistics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore techniques for analyzing data with multiple variables, such as multiple regression, factor analysis, and principal component analysis.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.Markdown(
            "[Multivariate Statistics](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Experimental Design         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Study the principles of experimental design and how to plan and analyze experiments to draw meaningful conclusions.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Experimental Design](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Time Series Analysis         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn about methods for analyzing and forecasting time-dependent data.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Time Series Analysis](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
        height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Bayesian Statistics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Introduce yourself to Bayesian methods, which involve updating probabilities based on new data.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Bayesian Statistics](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Nonparametric Statistics           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study statistical methods that make fewer assumptions about the underlying data distribution.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Nonparametric Statistics](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Data Mining and Machine Learning         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore techniques for analyzing large datasets and making predictions using machine learning algorithms.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Data Mining and Machine Learning](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Statistical Software        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Courses that focus on using statistical software like R, Python, SPSS, or SAS to perform data analysis and statistical modeling.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Statistical Software](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Biostatistics        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("A specialized course that applies statistical methods to medical and biological research.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    
        ft.Markdown(
            "[Biostatistics](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Business Analytics         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn how statistics is applied in business decision-making and data-driven strategies.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Business Analytics](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    





       

 ft.Divider(),









 ft.Text("BIOCHEMISTRY",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Introduction to Biochemistry         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("A foundational course that provides an overview of the principles and fundamentals of biochemistry.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                ft.Markdown(
            "[Introduction to Biochemistry](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Cell Biology        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                     ft.Text("Study the structure and function of cells, including cellular organelles, membrane transport, and cellular processes.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Cell Biology](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Molecular Biology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore the molecular mechanisms of genetic information flow, including DNA replication, transcription, and translation.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Molecular Biology](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Enzymology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn about enzymes, their kinetics, and their role in catalyzing biochemical reactions.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.Markdown(
            "[Enzymology](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Metabolism         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Study the metabolic pathways involved in the synthesis and breakdown of biomolecules in cells.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Metabolism](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Biochemical Techniques         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Gain practical skills in various laboratory techniques commonly used in biochemistry research.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Biochemical Techniques](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Protein Structure and Function         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Focus on the structure, folding, and functions of proteins in living organisms.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Protein Structure and Function](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Nucleic Acids           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore the structure and function of DNA and RNA, including gene expression and regulation.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Nucleic Acids](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Lipids and Membrane Biology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study the structure and functions of lipids and membranes in cells.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Lipids and Membrane Biology](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Bioinformatics       ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn how to analyze biological data using computational tools and databases.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Bioinformatics](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Immunology        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Study the immune system and its interactions with biochemical processes in disease and immunity.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    
        ft.Markdown(
            "[Immunology](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Biochemistry of Disease        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore how biochemistry is involved in the development and progression of various diseases.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Biochemistry of Disease](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    




 

       

 ft.Divider(),






 ft.Text("ARTS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Drawing and Sketching         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("A fundamental course that teaches the basics of drawing, sketching techniques, and observational skills.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                ft.Markdown(
            "[Drawing and Sketching](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Painting        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                     ft.Text("Courses that explore different painting mediums such as watercolor, acrylic, oil, and gouache, and various painting styles and techniques.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Painting](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Sculpture         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Learn the art of sculpting in various materials like clay, wood, metal, or stone, and explore both traditional and contemporary approaches.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Sculpture](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Photography         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Courses that cover the basics of photography, composition, lighting, and post-processing techniques.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.Markdown(
            "[Photography](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Graphic Design         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Learn about design principles, typography, layout, and software skills to create visual communication pieces.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Graphic Design](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Digital Illustration         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Courses that focus on creating illustrations using digital tools and software.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Digital Illustration](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Printmaking         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore traditional printmaking techniques like linocut, etching, and screen printing.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Printmaking](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Art History           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Study the evolution of art, major art movements, and influential artists throughout history.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Art History](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Art Appreciation         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Courses that help you develop a deeper understanding and appreciation of art and its cultural significance.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Art Appreciation](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Performing Arts (Theatre, Dance, Music)        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Courses that cover different aspects of performing arts, including acting, dance styles, music theory, and performance techniques.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Performing Arts (Theatre, Dance, Music)](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Animation        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("Learn the principles of animation and how to create animated characters and scenes.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    
        ft.Markdown(
            "[Animation](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Film Studies         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("Explore the art of filmmaking, including storytelling, cinematography, and film analysis.       ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Film Studies](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    




 

      
 ft.Divider(),







                 ft.Text("AGRICULTURE",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),










            

                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Introduction to Agriculture         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                   ft.Text("A fundamental course that covers the basics of agriculture, including the history of agriculture, crop production, soil science, and agricultural economics.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                ft.Markdown(
            "[Introduction to Agriculture](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


        
             ft.Container(
                    content=ft.Column([ft.Text("Crop Science        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                        ft.Text("This course focuses on plant biology, agronomy, and crop management techniques to maximize crop yields and quality.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                     ft.Markdown(
            "[Crop Science](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




                  
         ft.Container(
                    content=ft.Column([ft.Text("Animal Science         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                      ft.Text("This course delves into animal husbandry, livestock production, nutrition, breeding, and disease management.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                     ft.Markdown(
            "[Animal Science](https://drive.google.com/drive/folders/107GwxuxTxv4o4iqtWM5Btf1cpjDPjXxd)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,


                

                ft.Container(
                    content=ft.Column([ft.Text("Agribusiness Management         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                      ft.Text("An essential course for understanding the business side of agriculture, covering topics such as marketing, finance, supply chain management, and agricultural economics.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                   ft.Markdown(
            "[Agribusiness Management](https://drive.google.com/drive/folders/13lU_82wGTFJafOgojwN-s9UH9scFX9kZ)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),
                    ]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,
      




                 ft.Container(
                    content=ft.Column([ft.Text("Agricultural Engineering         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                       ft.Text("This course explores the application of engineering principles to design and develop agricultural machinery, irrigation systems, and other agricultural technologies.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                     ft.Markdown(
            "[Agricultural Engineering](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,






                   ft.Container(
                    content=ft.Column([ft.Text("Sustainable Agriculture         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                      ft.Text("A course that emphasizes environmentally friendly and sustainable farming practices, including organic farming, conservation agriculture, and integrated pest management.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                    ft.Markdown(
            "[Sustainable Agriculture](https://drive.google.com/drive/folders/18b_pO7lo4JdVbkKMA18Ck1mzNnsuJbuf)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                 width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                
                ) ,



                    ft.Container(
                    content=ft.Column([ft.Text("Agricultural Extension and Rural Development         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                                      ft.Text("This course focuses on reaching out to farmers and rural communities to provide them with the latest agricultural knowledge and practices for better productivity and livelihoods.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),

                     ft.Markdown(
            "[Agricultural Extension and Rural Development](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,





                      ft.Container(
                    content=ft.Column([ft.Text("Agricultural Economics           ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("This course explores the economic aspects of agriculture, including resource allocation, agricultural policy, and international trade in agricultural products.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                     ft.Markdown(
            "[Agricultural Economics](https://drive.google.com/drive/folders/1JhhszyZTK2josxKK4Rcs2o11TE_FBl-F)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,




              ft.Container(
                    content=ft.Column([ft.Text("Soil Science         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("This course delves into the properties and management of soils, including soil fertility, soil conservation, and soil testing.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    ft.Markdown(
            "[Soil Science](https://drive.google.com/drive/folders/1hWenZPufyrQ4QSt4Z2KHI-hQLwjvHfUq)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                    height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ) ,



                       ft.Container(
                    content=ft.Column([ft.Text("Horticulture        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("A specialized course that focuses on the cultivation of fruits, vegetables, and ornamental plants.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                
        ft.Markdown(
            "[Horticulture](https://drive.google.com/drive/folders/1BdZdl-zjLSUitAs8PYXq-vK234Ap5023)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
                height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
        
                ) ,




                   ft.Container(
                    content=ft.Column([ft.Text("Precision Agriculture        ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                    ft.Text("This course explores the use of technology, including remote sensing, GPS, and data analysis, to optimize farm management practices and increase efficiency.   ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                    
        ft.Markdown(
            "[Precision Agriculture](https://drive.google.com/drive/folders/188LlOrJx4A_eOt_haK4iSB8vE1517Gm0)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),
                    
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
            
                ) ,



                     ft.Container(
                    content=ft.Column([ft.Text("Food Science and Technology         ",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   ft.Text("A course that covers the science behind food processing, preservation, and quality assurance in the agricultural and food industries.         ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   
        ft.Markdown(
            "[Food Science and Technology](https://drive.google.com/drive/folders/1ckOEos_onAK7xveXypuOi-x9pLm3wXzO)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),]),

                   
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    width=400,
            height=200,
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                ) ,







           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),

    




       



        
    


                ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )










































































































































              #quiz



        if page.route == "/quiz":
            page.views.append(
                ft.View(
                    "/quiz",
                    [
                        ft.AppBar(title=ft.Text("Quiz"), bgcolor=ft.colors.BLUE_900),
                        




                        ft.Image(src="q2.png",border_radius=30,fit=ft.ImageFit.COVER,),

                        ft.Text("SAMPLE QUESTIONS",weight=ft.FontWeight.BOLD, color="white",style=ft.TextThemeStyle.HEADLINE_MEDIUM ),
    

    


    
        ft.Container(
                    content=ft.Text("Choose a course to start an EXERCISE with us on WEMO"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                    
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                    
                ),  
      
    
    
    







                    ft.Text("COMPUTER SCIENCE",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),


















                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("JAVA       QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("JAVA", on_click=lambda _: page.go("/java")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("DATABASE       QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("DATABASE", on_click=lambda _: page.go("/database")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("OPEN SOURCE      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("OPEN SOURCE", on_click=lambda _: page.go("/opensourse")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("VISUAL STUDIOS      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("VISUAL STUDIOS", on_click=lambda _: page.go("/vs")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("MOBILE APP      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("MOBILE APP", on_click=lambda _: page.go("/mobileapp")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("OPERATION RESEARCH       QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("OPERATION RESEARCH", on_click=lambda _: page.go("/or")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



 ft.Container(
              content=ft.Column([
                  ft.Text("WEB BASED DEVL.       QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("WEB BASED DEVL", on_click=lambda _: page.go("/wb")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




         ft.Container(
              content=ft.Column([
                  ft.Text("DATA STRUCTURES       QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("DATA STRUCTURES ", on_click=lambda _: page.go("/ds")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),











        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),



    
 

    ft.Divider(),
    
        
 ft.Text("NATURAL RESOURCES",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),

      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Environmental Science      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Environmental Science", on_click=lambda _: page.go("/es")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Conservation Biology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Conservation Biology", on_click=lambda _: page.go("/cb")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Sustainable Resource Management     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Sustainable Resource Management", on_click=lambda _: page.go("/srm")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Environmental Policy and Law      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Environmental Policy and Law", on_click=lambda _: page.go("/epl")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Geographic Information Systems (GIS) and Remote Sensing      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Geographic Information Systems (GIS) and Remote Sensing", on_click=lambda _: page.go("/gis")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Natural Resource Economics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Natural Resource Economics", on_click=lambda _: page.go("/nre")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        
ft.Container(
              content=ft.Column([
                  ft.Text("Renewable Energy and Sustainability      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Renewable Energy and Sustainability", on_click=lambda _: page.go("/res")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),
              




              
ft.Container(
              content=ft.Column([
                  ft.Text("Soil and Water Resources Management      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Soil and Water Resources Management", on_click=lambda _: page.go("/swrm")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),








        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),






    ft.Divider(),




 ft.Text("OPTOMETRY",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),

             


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Anatomy and Physiology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Anatomy and Physiology", on_click=lambda _: page.go("/ap")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Ocular Biology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Ocular Biology", on_click=lambda _: page.go("/ob")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Optics and Refraction     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Optics and Refraction", on_click=lambda _: page.go("/opr")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Visual Optics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Visual Optics", on_click=lambda _: page.go("/vo")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Ocular Disease and Pathology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Ocular Disease and Pathology", on_click=lambda _: page.go("/odp")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Binocular Vision and Vision Therapy      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Binocular Vision and Vision Therapy", on_click=lambda _: page.go("/bvvt")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        

                  
ft.Container(
              content=ft.Column([
                  ft.Text("Pharmacology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Pharmacology", on_click=lambda _: page.go("/pha")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),








          
ft.Container(
              content=ft.Column([
                  ft.Text("Pediatric Optometry      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Pediatric Optometry", on_click=lambda _: page.go("/pop")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),






        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),








 

    ft.Divider(),




 ft.Text("PHYSICS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),

           


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Classical Mechanics     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Classical Mechanics", on_click=lambda _: page.go("/clm")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Electromagnetism      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Electromagnetism", on_click=lambda _: page.go("/elt")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Quantum Mechanics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Quantum Mechanics", on_click=lambda _: page.go("/qum")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Thermodynamics and Statistical Mechanics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Thermodynamics and Statistical Mechanics", on_click=lambda _: page.go("/tsm")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Optics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Optics", on_click=lambda _: page.go("/opt")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Modern Physics     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Modern Physics", on_click=lambda _: page.go("/mop")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        
                    
ft.Container(
              content=ft.Column([
                  ft.Text("Solid State Physics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Solid State Physics", on_click=lambda _: page.go("/ssp")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),









               
ft.Container(
              content=ft.Column([
                  ft.Text("Fluid Mechanics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Fluid Mechanics", on_click=lambda _: page.go("/fum")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),







        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),










    ft.Divider(),







 ft.Text("MATHEMATICS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
          


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Calculus     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Calculus", on_click=lambda _: page.go("/cal")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Linear Algebra      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Linear Algebra", on_click=lambda _: page.go("/lig")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Discrete Mathematics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Discrete Mathematics", on_click=lambda _: page.go("/dim")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Probability and Statistics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Probability and Statistics", on_click=lambda _: page.go("/pas")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Number Theory      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Number Theory", on_click=lambda _: page.go("/nut")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Differential Equations      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Differential Equations", on_click=lambda _: page.go("/diq")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        
               
ft.Container(
              content=ft.Column([
                  ft.Text("Real Analysis      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Real Analysis", on_click=lambda _: page.go("/rea")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



                    
ft.Container(
              content=ft.Column([
                  ft.Text("Abstract Algebra     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Abstract Algebra", on_click=lambda _: page.go("/aba")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),







        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),










    ft.Divider(),






 ft.Text("CHEMISTRY",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),



            


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("General Chemistry      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("General Chemistry", on_click=lambda _: page.go("/gec")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Organic Chemistry      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Organic Chemistry", on_click=lambda _: page.go("/ogc")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Inorganic Chemistry     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Inorganic Chemistry", on_click=lambda _: page.go("/inc")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Physical Chemistry      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Physical Chemistry", on_click=lambda _: page.go("/phc")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Analytical Chemistry      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Analytical Chemistry", on_click=lambda _: page.go("/anc")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Biochemistry      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Biochemistry", on_click=lambda _: page.go("/bic")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        
                        
ft.Container(
              content=ft.Column([
                  ft.Text("Environmental Chemistry      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Environmental Chemistry", on_click=lambda _: page.go("/enc")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


                      
ft.Container(
              content=ft.Column([
                  ft.Text("Computational Chemistry     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Computational Chemistry", on_click=lambda _: page.go("/coc")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),





        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),










 

    ft.Divider(),




 ft.Text("STATISTICS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
             


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Statistical Inference     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Statistical Inference", on_click=lambda _: page.go("/sin")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Regression Analysis      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Regression Analysis", on_click=lambda _: page.go("/ren")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Multivariate Statistics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Multivariate Statistics", on_click=lambda _: page.go("/mus")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Experimental Design      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Experimental Design", on_click=lambda _: page.go("/epd")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Time Series Analysis      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Time Series Analysis", on_click=lambda _: page.go("/tsa")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Bayesian Statistics     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Bayesian Statistics", on_click=lambda _: page.go("/bas")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        


               
ft.Container(
              content=ft.Column([
                  ft.Text("Nonparametric Statistics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Nonparametric Statistics", on_click=lambda _: page.go("/nos")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),








                     
ft.Container(
              content=ft.Column([
                  ft.Text("Data Mining and Machine Learning      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Data Mining and Machine Learning", on_click=lambda _: page.go("/dmml")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),





        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),











    ft.Divider(),



 ft.Text("BIOCHEMISTRY",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
             


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Cell Biology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Cell Biology", on_click=lambda _: page.go("/ceb")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Molecular Biology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Molecular Biology", on_click=lambda _: page.go("/mob")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Enzymology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Enzymology", on_click=lambda _: page.go("/enz")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Metabolism      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Metabolism", on_click=lambda _: page.go("/met")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Biochemical Techniques      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Biochemical Techniques", on_click=lambda _: page.go("/bit")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Protein Structure and Function     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Protein Structure and Function", on_click=lambda _: page.go("/psf")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




         
ft.Container(
              content=ft.Column([
                  ft.Text("Nucleic Acids      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Nucleic Acids", on_click=lambda _: page.go("/nua")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



              
ft.Container(
              content=ft.Column([
                  ft.Text("Lipids and Membrane Biology      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Lipids and Membrane Biology", on_click=lambda _: page.go("/lmb")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),





        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),





         
    ft.Divider(),



 ft.Text("ARTS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
             


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Drawing and Sketching     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Drawing and Sketching", on_click=lambda _: page.go("/das")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Painting     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Painting", on_click=lambda _: page.go("/paint")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Sculpture      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Sculpture", on_click=lambda _: page.go("/sup")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Photography      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Photography", on_click=lambda _: page.go("/photo")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Graphic Design      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Graphic Design", on_click=lambda _: page.go("/gad")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Digital Illustration     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Digital Illustration", on_click=lambda _: page.go("/dil")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




         
ft.Container(
              content=ft.Column([
                  ft.Text("Printmaking      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Printmaking", on_click=lambda _: page.go("/print")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




           
ft.Container(
              content=ft.Column([
                  ft.Text("Art History     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Art History", on_click=lambda _: page.go("/art")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),






                 
    ft.Divider(),



 ft.Text("AGRICULTURE",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
             


      
                     ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("Crop Science     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Crop Science", on_click=lambda _: page.go("/cos")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




ft.Container(
              content=ft.Column([
                  ft.Text("Animal Science      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Animal Science", on_click=lambda _: page.go("/ans")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Agribusiness Management      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Agribusiness Management", on_click=lambda _: page.go("/agm")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Agricultural Engineering      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Agricultural Engineering", on_click=lambda _: page.go("/age")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        ft.Container(
              content=ft.Column([
                  ft.Text("Sustainable Agriculture     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Sustainable Agriculture", on_click=lambda _: page.go("/sua")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("Agricultural Extension and Rural Development     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Agricultural Extension and Rural Development", on_click=lambda _: page.go("/aerd")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),



      
ft.Container(
              content=ft.Column([
                  ft.Text("Agricultural Economics      QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Agricultural Economics", on_click=lambda _: page.go("/aec")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),




        
ft.Container(
              content=ft.Column([
                  ft.Text("Soil Science     QUESTIONS",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                   ft.TextButton("Soil Science", on_click=lambda _: page.go("/soil")), 
                    
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),

        







        
                     ],spacing=0,alignment=ft.alignment.center,scroll=ft.ScrollMode.ALWAYS ),









                        

                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()






































































































































       #menu



        if page.route == "/menu":
            page.views.append(
                ft.View(
                    "/menu",
                    [
                        ft.AppBar(title=ft.Text("MENU"), bgcolor=ft.colors.BLUE_900),
                        





                     ft.Container(
            padding=ft.padding.all(4),
            border=ft.border.all(5,"white"),
            border_radius=ft.border_radius.all(10000),
            content=ft.Text("WEMO",color="white",size=50)
            ),
        
                        
   
    
    
    ft.Text(""),
 
 
    
   
   

    


    
    ft.Text(""),
    ft.Text(""), 
    
    
            ft.Text("LOG IN/LOG OUT or REGISTER",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   

        ft.Container(
              content=ft.Column([
        ft.Markdown(
            "[LOG IN/LOG OUT or REGISTER](https://accounts.google.com/v3/signin/identifier?dsh=S1527517263%3A1690387224733863&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Den-US&ec=GAlA8wE&hl=en&flowName=GlifWebSignIn&flowEntry=AddSession)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="androidstudio",
        ),

         ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),

 ft.Divider(),
       




      ft.Text("Contact informations of TUTORS",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   


        

       ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("COMPUTER SCIENCE TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: Bsc. Com. Science",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


         
ft.Container(
              content=ft.Column([
                  ft.Text("AGRICULTURE TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: Bsc. Agriculture ",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),






        ft.Container(
              content=ft.Column([
                  ft.Text("ARTS TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: BA. Integrated Rural Art and Industry",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),
         
         ft.Container(
              content=ft.Column([
                  ft.Text("BIOCHEMISTRY TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: Bsc. Biochemistry",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),





           ft.Container(
              content=ft.Column([
                  ft.Text("STATISTICS TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: Bsc. Statistics",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),  



        ft.Container(
              content=ft.Column([
                  ft.Text("CHEMISTRY TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: Bsc. Chemistry",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),

        ft.Container(
              content=ft.Column([
                  ft.Text("OPTOMETRY TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification:Doctor pf Optometry",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                     
        ),



        ft.Container(
              content=ft.Column([
                  ft.Text("PHYSICS TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: Bsc. Physics",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),






        ft.Container(
              content=ft.Column([
                  ft.Text("MATHEMATICS TUTOR",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Text("Name:Loshar Hammond",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Qualification: Bsc. matimathics",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Phone: 0505264636",style=ft.TextThemeStyle.LABEL_MEDIUM),
                 ft.Text("Email: kekelibluesky.com",style=ft.TextThemeStyle.LABEL_MEDIUM),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),












       ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),


 ft.Divider(),














ft.Text("RECOMMENDED COURSES",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   

















                ft.Row([ ft.Container(
              content=ft.Column([
                  ft.Text("COMPUTER SCIENCE ",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Markdown(
            "[JAVA](https://drive.google.com/drive/folders/1QF6mvTPlo0XVG9HgIPuqAAhEN86bszot)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[DATABASE](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[MOBILE APPS](https://drive.google.com/drive/folders/1FOOALEBaXRDq6wWbxnlgxfm5jhF117EI)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[VISUAL STUDIO](https://drive.google.com/drive/folders/10DdhxjOnJuOPv8tHPcuGVPMA8mjsfw81)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),


         
ft.Container(
              content=ft.Column([
                  ft.Text("AGRICULTURE",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
               ft.Markdown(
            "[Crop Science](www.cropscience.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[Agribusiness ](www.agribusiness.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[Horticulture](https://Horticulture.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[Soil Science](https://Soilscience.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),
              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                     
        ),



            ft.Container(
              content=ft.Column([
                  ft.Text("ARTS",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Markdown(
            "[Fashion Design](https://FashionDesign.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[Film Studies](https://FilmStudies.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[Art Therapy](https://ArtTherapy.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[Sculpture](https://Sculpture.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
              
        ),









          ft.Container(
              content=ft.Column([
                  ft.Text("MATIMATICS",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Markdown(
            "[Topology](https://Topology.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[Numerical Analysis](https://NumericalAnalysis.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[Actuarial Mathematics](https://ActuarialMathematics.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[Complex Analysis](https://ComplexAnalysis.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
          
        ),




                       ft.Container(
              content=ft.Column([
                  ft.Text("OPTOMETRY",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Markdown(
            "[Pharmacology](https://Pharmacology.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[Visual Optics](https://VisualOptics.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[Ocular Biology](https://OcularBiology.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[Anatomy and Physiology](https://AnatomyandPhysiology.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                     
        ),
  




           

            ft.Container(
              content=ft.Column([
                  ft.Text("CHEMISTRY",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Markdown(
            "[Computational Chemistry](https://ComputationalChemistry.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[Medicinal Chemistry](https://MedicinalChemistry.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[Quantum Chemistry](https://QuantumChemistry.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[Food Chemistry](https://FoodChemistry.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                     
        ),
     












                           ft.Container(
              content=ft.Column([
                  ft.Text("STATISTICS",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Markdown(
            "[Regression Analysis](https://RegressionAnalysis.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[Multivariate Statistics](https://MultivariateStatistics.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[Biostatistics](https://Biostatistics.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[Business Analytics](https://BusinessAnalytics.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                     
        ),
  
















                  ft.Container(
              content=ft.Column([
                  ft.Text("BIOCHEMISTRY",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                ft.Markdown(
            "[Cell Biology](https://CellBiology.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atom-one-dark",
        ),
 
              ft.Markdown(
            "[Enzymology](https://Enzymology.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-plateau-light",
        ),  

        ft.Markdown(
            "[Bioinformatics](https://Bioinformatics.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="a11y-light",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
        ),

        ft.Markdown(
            "[Nucleic Acids](https://NucleicAcids.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

              ]),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLUE_900,
                
                    
                    shadow=ft.BoxShadow(
        spread_radius=1,
        blur_radius=15,
        color=ft.colors.BLACK,
        offset=ft.Offset(0, 0),
        blur_style=ft.ShadowBlurStyle.OUTER,
    ),
                    border_radius=10,
                      
        ),
 












           ] ,spacing=2,alignment=ft.alignment.center,scroll = ft.ScrollMode.ALWAYS),
       
 ft.Divider(),
















                ft.Text("RECOMMENDED SITES",color="white",style=ft.TextThemeStyle.HEADLINE_SMALL,weight="bold"),
                   

                   ft.Row([
                        ft.Markdown(
            "[Coursera](www.coursera.org)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[Khan Academy](www.khanacademy.org)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[W3school](https://www.w3schools.com/)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


                   ],alignment=ft.alignment.center),




                   ft.Row([
                        ft.Markdown(
            "[Alison](www.alison.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[Udemy](www.udemy.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[edX](www.edx.org)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


                   ],alignment=ft.alignment.center),
        


        ft.Row([
                        ft.Markdown(
            "[Codecademy](www.codecademy.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[Duolingo](www.duolingo.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[TED-Ed](www.ed.ted.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


                   ],alignment=ft.alignment.center),
        


        ft.Row([
                        ft.Markdown(
            "[National Geographic Kids](www.kids.nationalgeographic.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[Crash Course](www.crashcourse.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


       

                   ],alignment=ft.alignment.center),







             ft.Row([
                       

         ft.Markdown(
            "[MIT OpenCourseWare](ocw.mit.edu)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


                   ],alignment=ft.alignment.center),







        

ft.Row([
                        ft.Markdown(
            "[Academic Earth](www.academicearth.org)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         ft.Markdown(
            "[Google Arts & Culture](www.artsandculture.google.com)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),


         

        

                   ],alignment=ft.alignment.center),
        
              



                    ft.Row([
                       

         ft.Markdown(
            "[NASA's website for education](www.nasa.gov/education)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),
         
          ft.Markdown(
            "[History for Kids](www.historyforkids.net)",
            extension_set="gitHubWeb",
            on_tap_link=open_url,
            expand=False,
            code_theme="atelier-lakeside-light",

        ),

        

                   ],alignment=ft.alignment.center),
        




        
       
 ft.Divider(),










                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        page.update()

























































































































               #computer science questions

              #java


        if page.route == "/java":
            page.views.append(
                ft.View(
                    "/java",
                    [
                        ft.AppBar(title=ft.Text("JAVA"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/database":
            page.views.append(
                ft.View(
                    "/database",
                    [
                        ft.AppBar(title=ft.Text("DATABASE"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1.Which of the following is NOT a type of database model? ?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Relational", on_click=on_click1,),
             ft.TextButton(text="b) Hierarchical",on_click=on_click1),
             ft.TextButton(text="c) Object-Oriented",on_click=on_click1,),
             ft.TextButton(text="d) Linear ", on_click=on_click2,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2. In a relational database, what is a primary key? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) A key used for encryption", on_click=on_click1,),
             ft.TextButton(text="b) A key used for data backup",on_click=on_click1),
             ft.TextButton(text="c) A unique identifier for a record in a table",on_click=on_click2,),
             ft.TextButton(text="d) A key used to access the database remotely", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. What does SQL stand for in the context of DBMS? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Sequential Query Language", on_click=on_click1,),
             ft.TextButton(text="b) Structured Query Logic",on_click=on_click1),
             ft.TextButton(text="c) Simple Query Language",on_click=on_click1,),
             ft.TextButton(text="d) Structured Query Language ", on_click=on_click2,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. Which type of join returns all the rows from both tables, matching rows from the left table with NULL values in the right table for non-matching rows? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) INNER JOIN", on_click=on_click1,),
             ft.TextButton(text="b) RIGHT JOIN",on_click=on_click1),
             ft.TextButton(text="c) LEFT JOIN ",on_click=on_click2,),
             ft.TextButton(text="d) FULL JOIN", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. Which normal form ensures that there are no partial dependencies in a relational database? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) First Normal Form (1NF)", on_click=on_click1,),
             ft.TextButton(text="b) Second Normal Form (2NF)",on_click=on_click1),
             ft.TextButton(text="c) Third Normal Form (3NF) ",on_click=on_click2,),
             ft.TextButton(text="d) Boyce-Codd Normal Form (BCNF)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. In a DBMS, what is the purpose of an index? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To store backup copies of the database", on_click=on_click1,),
             ft.TextButton(text="b) To enforce referential integrity constraints",on_click=on_click1),
             ft.TextButton(text="c) To speed up data retrieval by providing quick access to specific data",on_click=on_click2,),
             ft.TextButton(text="d) To create a logical view of the database", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. What is a foreign key in a relational database? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) A key that is automatically generated for each record in a table", on_click=on_click1,),
             ft.TextButton(text="b) A key used to encrypt sensitive data",on_click=on_click1),
             ft.TextButton(text="c) A key used to establish a relationship between two tables ",on_click=on_click2,),
             ft.TextButton(text="d) A key used for data compression", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. Which database model is based on a tree-like structure with parent-child relationships between records? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Relational Model", on_click=on_click1,),
             ft.TextButton(text="b) Hierarchical Model",on_click=on_click2),
             ft.TextButton(text="c) Network Model",on_click=on_click1,),
             ft.TextButton(text="d) Object-Oriented Model", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which DBMS component is responsible for processing user queries and commands? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Database Engine", on_click=on_click2,),
             ft.TextButton(text="b) Data Dictionary",on_click=on_click1),
             ft.TextButton(text="c) Data Loader",on_click=on_click1,),
             ft.TextButton(text="d) Database Administrator", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. Which database constraint ensures that the value of a column is unique across all rows in a table? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Primary Key", on_click=on_click1,),
             ft.TextButton(text="b) Foreign Key",on_click=on_click1),
             ft.TextButton(text="c) Unique Key ",on_click=on_click2,),
             ft.TextButton(text="d) Check Constraint", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/opensourse":
            page.views.append(
                ft.View(
                    "/opensourse",
                    [
                        ft.AppBar(title=ft.Text("OPEN SOURSE OPERATING SYSTEM"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the main purpose of an operating system? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To provide hardware to the computer", on_click=on_click1,),
             ft.TextButton(text="b) To manage and coordinate computer hardware and software resources",on_click=on_click2),
             ft.TextButton(text="c) To protect the computer from viruses and malware",on_click=on_click1,),
             ft.TextButton(text="d) To manage the user interface of the computer", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2. Which of the following is NOT a function of an operating system? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Memory management", on_click=on_click1,),
             ft.TextButton(text="b) File management",on_click=on_click1),
             ft.TextButton(text="c) Database management",on_click=on_click1,),
             ft.TextButton(text="d) Process scheduling", on_click=on_click2,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. What is the role of the kernel in an operating system?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To manage the user interface", on_click=on_click1,),
             ft.TextButton(text="b) To provide hardware drivers",on_click=on_click1),
             ft.TextButton(text="c) To manage memory and process control",on_click=on_click2,),
             ft.TextButton(text="d) To execute application programs", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the purpose of virtual memory in an operating system? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To provide additional storage for files", on_click=on_click1,),
             ft.TextButton(text="b) To allow multiple users to access the system simultaneously",on_click=on_click1),
             ft.TextButton(text="c) To protect the operating system from malware",on_click=on_click1,),
             ft.TextButton(text="d) To extend the computer's RAM by using the hard disk as extra memory", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 5. Which scheduling algorithm is designed to give each process an equal amount of CPU time before moving to the next process? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) First-Come, First-Served (FCFS)", on_click=on_click1,),
             ft.TextButton(text="b) Shortest Job Next (SJN)",on_click=on_click1),
             ft.TextButton(text="c) Round Robin",on_click=on_click2,),
             ft.TextButton(text="d) Priority Scheduling", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6.What is a context switch in the context of operating systems? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) The process of switching between different user accounts", on_click=on_click1,),
             ft.TextButton(text="b) The process of switching between different applications running on the computer",on_click=on_click1),
             ft.TextButton(text="c) The process of switching between kernel mode and user mode",on_click=on_click1,),
             ft.TextButton(text="d) The process of saving the current state of a process and loading the state of another process", on_click=on_click2,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Which file system is commonly used in Windows operating systems? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) FAT32", on_click=on_click1,),
             ft.TextButton(text="b) NTFS ",on_click=on_click2),
             ft.TextButton(text="c) Ext4",on_click=on_click1,),
             ft.TextButton(text="d) HFS+", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the purpose of an interrupt in an operating system? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To initiate a system shutdown", on_click=on_click1,),
             ft.TextButton(text="b) To stop a running process",on_click=on_click1),
             ft.TextButton(text="c) To request the attention of the operating system for a specific task ",on_click=on_click2,),
             ft.TextButton(text="d) To send a message to another user on the network", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.Which process scheduling algorithm selects the process with the shortest burst time for execution? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) First-Come, First-Served (FCFS)", on_click=on_click1,),
             ft.TextButton(text="b) Shortest Job Next (SJN)",on_click=on_click2),
             ft.TextButton(text="c) Round Robin",on_click=on_click1,),
             ft.TextButton(text="d) Priority Scheduling", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is a deadlock in the context of operating systems? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) A process that is waiting for resources indefinitely, and the resources are never released", on_click=on_click2,),
             ft.TextButton(text="b) A process that has been terminated by the operating system",on_click=on_click1),
             ft.TextButton(text="c) A process that is consuming too much CPU time",on_click=on_click1,),
             ft.TextButton(text="d) A process that is waiting for user input", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/vs":
            page.views.append(
                ft.View(
                    "/vs",
                    [
                        ft.AppBar(title=ft.Text("VISUAL BASICS"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is Visual Basic (VB)? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) A scripting language used for web development", on_click=on_click1,),
             ft.TextButton(text="b) A programming language developed by Microsoft for building Windows applications",on_click=on_click2),
             ft.TextButton(text="c) A markup language for creating web pages",on_click=on_click1,),
             ft.TextButton(text="d) A database management system", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2. What is the extension of Visual Basic project files?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) .exe", on_click=on_click1,),
             ft.TextButton(text="b) .docx",on_click=on_click1),
             ft.TextButton(text="c) .vbproj ",on_click=on_click2,),
             ft.TextButton(text="d) .html", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which component is used to display messages to the user in a Visual Basic application?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) MessageBox", on_click=on_click1,),
             ft.TextButton(text="b) InputBox",on_click=on_click1),
             ft.TextButton(text="c) PrintBox",on_click=on_click1,),
             ft.TextButton(text="d) MsgBox", on_click=on_click2,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. How do you declare a variable in Visual Basic? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) var myVariable", on_click=on_click1,),
             ft.TextButton(text="b) Dim myVariable",on_click=on_click2),
             ft.TextButton(text="c) int myVariable",on_click=on_click1,),
             ft.TextButton(text="d) Variable myVariable", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. Which event occurs when a user clicks a button on a form in a Visual Basic application? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Load", on_click=on_click1,),
             ft.TextButton(text="b) MouseClick",on_click=on_click1),
             ft.TextButton(text="c) Click ",on_click=on_click2,),
             ft.TextButton(text="d) Activate", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What is the purpose of the 'Handles' keyword in a Visual Basic event handler?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) It indicates the type of data the event handler will return.", on_click=on_click1,),
             ft.TextButton(text="b) It specifies the name of the event that the handler will respond to. ",on_click=on_click2),
             ft.TextButton(text="c) It creates a new variable to store event data.",on_click=on_click1,),
             ft.TextButton(text="d) It is used to define the scope of the event handler.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. How do you add a comment in Visual Basic? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) // This is a comment", on_click=on_click1,),
             ft.TextButton(text="b) /* This is a comment */",on_click=on_click1),
             ft.TextButton(text="c) ' This is a comment",on_click=on_click2,),
             ft.TextButton(text="d) <!-- This is a comment -->", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8.Which control is used to display multiple lines of text in a Visual Basic application?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) TextBox", on_click=on_click1,),
             ft.TextButton(text="b) Label",on_click=on_click1),
             ft.TextButton(text="c) ListBox",on_click=on_click2,),
             ft.TextButton(text="d) Button", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which statement is used to end a Visual Basic program? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) exit", on_click=on_click1,),
             ft.TextButton(text="b) finish",on_click=on_click1),
             ft.TextButton(text="c) end",on_click=on_click2,),
             ft.TextButton(text="d) terminate", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. How do you open the code window for a form in a Visual Basic project?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Right-click on the form and select 'Open Code Window.'", on_click=on_click1,),
             ft.TextButton(text="b) Click on the 'File' menu and choose 'Open Code Window.'",on_click=on_click1),
             ft.TextButton(text="c) Double-click on the form in the Solution Explorer.",on_click=on_click2,),
             ft.TextButton(text="d) Press F5 on the keyboard.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/mobileapp":
            page.views.append(
                ft.View(
                    "/mobileapp",
                    [
                        ft.AppBar(title=ft.Text("MOBILE APPS"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which programming language is commonly used for Android app development?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Swift", on_click=on_click1,),
             ft.TextButton(text="b) Java ",on_click=on_click2),
             ft.TextButton(text="c) Objective-C",on_click=on_click1,),
             ft.TextButton(text="d) C#", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2. What is the purpose of the AndroidManifest.xml file in Android app development? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) It contains the user interface elements of the app.", on_click=on_click1,),
             ft.TextButton(text="b) It stores the app's data and resources.",on_click=on_click1),
             ft.TextButton(text="c) It defines the structure and components of the app and its permissions. ",on_click=on_click2,),
             ft.TextButton(text="d) It handles the backend logic of the app.", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. What is an APK in the context of Android app development? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) An Android Package Kit, which contains the source code of the app.", on_click=on_click1,),
             ft.TextButton(text="b) A file format for audio and video files in Android apps.",on_click=on_click1),
             ft.TextButton(text="c) An app bundle that includes all the resources and code required for the app installation. ",on_click=on_click2,),
             ft.TextButton(text="d) An archive file containing images and media assets used in the app.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. In iOS app development, which programming language is used primarily? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Java", on_click=on_click1,),
             ft.TextButton(text="b) C++",on_click=on_click1),
             ft.TextButton(text="c) Swift",on_click=on_click2,),
             ft.TextButton(text="d) Python", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. Which integrated development environment (IDE) is commonly used for Android app development?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
                          
            ft.TextButton(text="a) Visual Studio", on_click=on_click1,),
             ft.TextButton(text="b) Eclipse",on_click=on_click1),
             ft.TextButton(text="c) Xcode",on_click=on_click1,),
             ft.TextButton(text="d) Android Studio ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What is the purpose of Interface Builder in iOS app development? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To design the app's user interface visually.", on_click=on_click1,),
             ft.TextButton(text="b) To write code for app functionality.",on_click=on_click1),
             ft.TextButton(text="c) To test the app on different devices.",on_click=on_click1,),
             ft.TextButton(text="d) To manage the database of the app.", on_click=on_click2,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Which programming language is commonly used for cross-platform mobile app development? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Java", on_click=on_click1,),
             ft.TextButton(text="b) C#",on_click=on_click1),
             ft.TextButton(text="c) Swift",on_click=on_click1,),
             ft.TextButton(text="d) JavaScript", on_click=on_click2,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the purpose of a storyboard in iOS app development? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To handle app navigation and transitions between view controllers. ", on_click=on_click2,),
             ft.TextButton(text="b) To manage the data model of the app.",on_click=on_click1),
             ft.TextButton(text="c) To store the app's resources and media files.",on_click=on_click1,),
             ft.TextButton(text="d) To handle the background tasks of the app.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.  Which platform allows the development of apps for multiple operating systems using a single codebase? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Native app development", on_click=on_click1,),
             ft.TextButton(text="b) Hybrid app development",on_click=on_click1),
             ft.TextButton(text="c) Cross-platform app development ",on_click=on_click2,),
             ft.TextButton(text="d) Web app development", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is the role of Firebase in mobile app development?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To provide real-time database and backend services for apps. ", on_click=on_click1,),
             ft.TextButton(text="b) To handle the user interface design of the app.",on_click=on_click2),
             ft.TextButton(text="c) To manage the security and permissions of the app.",on_click=on_click1,),
             ft.TextButton(text="d) To test the app's performance and functionality.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/ds":
            page.views.append(
                ft.View(
                    "/ds",
                    [
                        ft.AppBar(title=ft.Text("DATA STRUCTURES"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary purpose of data structures? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To store and organize data for easy retrieval and manipulation ", on_click=on_click2,),
             ft.TextButton(text="b) To perform complex mathematical operations",on_click=on_click1),
             ft.TextButton(text="c) To provide security for data storage",on_click=on_click1,),
             ft.TextButton(text="d) To manage network connections", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2. Which data structure is used to implement a Last-In-First-Out (LIFO) policy? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Queue", on_click=on_click1,),
             ft.TextButton(text="b) Linked List",on_click=on_click1),
             ft.TextButton(text="c) Stack",on_click=on_click2,),
             ft.TextButton(text="d) Tree", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. What is the time complexity of searching an element in a sorted array using binary search? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) O(1)", on_click=on_click1,),
             ft.TextButton(text="b) O(log n) ",on_click=on_click2),
             ft.TextButton(text="c) O(n)",on_click=on_click1,),
             ft.TextButton(text="d) O(n log n)", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. Which data structure is best suited for implementing a dictionary with fast search, insert, and delete operations? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Stack", on_click=on_click1,),
             ft.TextButton(text="b) Queue",on_click=on_click1),
             ft.TextButton(text="c) Hash Table",on_click=on_click2,),
             ft.TextButton(text="d) Linked List", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.What is the maximum number of children that a node can have in a binary tree?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) 1", on_click=on_click1,),
             ft.TextButton(text="b) 2",on_click=on_click2),
             ft.TextButton(text="c) 3",on_click=on_click1,),
             ft.TextButton(text="d) 4", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. In a linked list, what is the role of the 'head' pointer? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) It points to the last node of the list.", on_click=on_click1,),
             ft.TextButton(text="b) It points to the middle node of the list.",on_click=on_click1),
             ft.TextButton(text="c) It points to the first node of the list. ",on_click=on_click2,),
             ft.TextButton(text="d) It is used to traverse the list backwards.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Which data structure is used to implement breadth-first search (BFS) in a graph?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Stack", on_click=on_click1,),
             ft.TextButton(text="b) Queue ",on_click=on_click2),
             ft.TextButton(text="c) Tree",on_click=on_click1,),
             ft.TextButton(text="d) Linked List", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8.  Which data structure represents a hierarchical relationship between elements in a tree-like structure? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Queue", on_click=on_click1,),
             ft.TextButton(text="b) Stack",on_click=on_click1),
             ft.TextButton(text="c) Graph",on_click=on_click1,),
             ft.TextButton(text="d) Tree", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 9.  Which sorting algorithm has the worst-case time complexity of O(n^2)?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Merge Sort", on_click=on_click1,),
             ft.TextButton(text="b) Quick Sort",on_click=on_click1),
             ft.TextButton(text="c) Bubble Sort",on_click=on_click2,),
             ft.TextButton(text="d) Insertion Sort", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  What is the primary advantage of using a hash table over other data structures for storing data? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) It has a faster insertion and deletion.", on_click=on_click1,),
             ft.TextButton(text="b) It automatically sorts the data.",on_click=on_click1),
             ft.TextButton(text="c) It provides efficient searching using a key-value pair.",on_click=on_click2,),
             ft.TextButton(text="d) It uses less memory than other data structures.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/wb":
            page.views.append(
                ft.View(
                    "/wb",
                    [
                        ft.AppBar(title=ft.Text("WEB BASED CONCEPTS AND DEVL."), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What does HTTP stand for in the context of web development? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) HyperText Markup Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Hypertext Transfer Protocol",on_click=on_click2),
             ft.TextButton(text="c) Hypertext Markup Language",on_click=on_click1,),
             ft.TextButton(text="d) HyperTransfer Text Protocol", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2. Which programming language is commonly used for front-end web development?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Java", on_click=on_click1,),
             ft.TextButton(text="b) Python",on_click=on_click1),
             ft.TextButton(text="c) JavaScript",on_click=on_click2,),
             ft.TextButton(text="d) C#", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3.  What is the purpose of CSS (Cascading Style Sheets) in web development?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To define the structure and layout of a web page", on_click=on_click1,),
             ft.TextButton(text="b) To create interactive elements and animations",on_click=on_click1),
             ft.TextButton(text="c) To add functionality to web pages",on_click=on_click1,),
             ft.TextButton(text="d) To define the presentation and styling of a web page", on_click=on_click2,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.  Which tag is used to define the structure of an HTML document's body section? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) <head>", on_click=on_click1,),
             ft.TextButton(text="b) <body>",on_click=on_click2),
             ft.TextButton(text="c) <title>",on_click=on_click1,),
             ft.TextButton(text="d) <html>", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.  What is the role of a web server in web development?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To design the user interface of a website", on_click=on_click1,),
             ft.TextButton(text="b) To store and manage the website's data",on_click=on_click1),
             ft.TextButton(text="c) To process client requests and serve web pages ",on_click=on_click2,),
             ft.TextButton(text="d) To manage the domain name of the website", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which type of database is commonly used in web development to store structured data? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Relational Database", on_click=on_click2,),
             ft.TextButton(text="b) NoSQL Database",on_click=on_click1),
             ft.TextButton(text="c) Hierarchical Database",on_click=on_click1,),
             ft.TextButton(text="d) Flat File Database", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. What is a responsive web design? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) A web design that uses JavaScript to add interactivity to web pages", on_click=on_click1,),
             ft.TextButton(text="b) A web design that adapts and scales to different screen sizes and devices",on_click=on_click2),
             ft.TextButton(text="c) A web design that uses only HTML for styling and layout",on_click=on_click1,),
             ft.TextButton(text="d) A web design that is optimized for search engine ranking", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. Which term refers to the process of improving a website's visibility on search engine result pages? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Web optimization", on_click=on_click1,),
             ft.TextButton(text="b) Website design",on_click=on_click1),
             ft.TextButton(text="c) Search engine optimization (SEO) ",on_click=on_click2,),
             ft.TextButton(text="d) Web analytics", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. What is the purpose of a cookie in web development?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To store a website's HTML and CSS files", on_click=on_click1,),
             ft.TextButton(text="b) To display personalized ads to website visitors",on_click=on_click1),
             ft.TextButton(text="c) To track and store user information and preferences ",on_click=on_click2,),
             ft.TextButton(text="d) To manage the website's domain name", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. Which technology is used to enable real-time communication between a web browser and a web server?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) PHP", on_click=on_click1,),
             ft.TextButton(text="b) AJAX",on_click=on_click1),
             ft.TextButton(text="c) WebSocket",on_click=on_click2,),
             ft.TextButton(text="d) XML", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/or":
            page.views.append(
                ft.View(
                    "/or",
                    [
                        ft.AppBar(title=ft.Text("OPERATION RESEARCH"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary goal of Operations Research? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To optimize operations in the military", on_click=on_click1,),
             ft.TextButton(text="b) To maximize profits in a business",on_click=on_click1),
             ft.TextButton(text="c) To use mathematical techniques to make better decisions",on_click=on_click2,),
             ft.TextButton(text="d) To develop advanced statistical models", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  Linear Programming is a technique used to: ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Find the best route in a transportation network", on_click=on_click1,),
             ft.TextButton(text="b) Solve optimization problems with linear constraints ",on_click=on_click2),
             ft.TextButton(text="c) Optimize project schedules",on_click=on_click1,),
             ft.TextButton(text="d) Analyze complex decision trees", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which method is used to find the optimal solution in Linear Programming? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Simplex method", on_click=on_click2,),
             ft.TextButton(text="b) Gradient descent",on_click=on_click1),
             ft.TextButton(text="c) Random search",on_click=on_click1,),
             ft.TextButton(text="d) Genetic algorithm", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the purpose of the 'slack' variable in Linear Programming? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) To represent the amount by which the objective function can be improved", on_click=on_click1,),
             ft.TextButton(text="b) To represent the surplus of resources in a constraint",on_click=on_click2),
             ft.TextButton(text="c) To indicate the total profit in the objective function",on_click=on_click1,),
             ft.TextButton(text="d) To handle negative values in the constraints", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.  Which type of optimization problem involves finding the minimum or maximum value of a function with no constraints? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Nonlinear programming", on_click=on_click1,),
             ft.TextButton(text="b) Integer programming",on_click=on_click1),
             ft.TextButton(text="c) Unconstrained optimization ",on_click=on_click2,),
             ft.TextButton(text="d) Stochastic programming", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6.  The 'Big M' method is used to handle: ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Unbounded optimization problems", on_click=on_click1,),
             ft.TextButton(text="b) Integer variables in Linear Programming",on_click=on_click1),
             ft.TextButton(text="c) Multiple optimal solutions in Linear Programming",on_click=on_click1,),
             ft.TextButton(text="d) Artificial variables in Linear Programming ", on_click=on_click2,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Which technique is used to solve multi-objective optimization problems? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Sensitivity analysis", on_click=on_click1,),
             ft.TextButton(text="b) Goal programming",on_click=on_click2),
             ft.TextButton(text="c) Transportation method",on_click=on_click1,),
             ft.TextButton(text="d) Integer programming", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. In queuing theory, the average number of customers waiting in a queue is called: ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Service rate", on_click=on_click1,),
             ft.TextButton(text="b) Utilization factor",on_click=on_click1),
             ft.TextButton(text="c) Arrival rate",on_click=on_click1,),
             ft.TextButton(text="d) Queue length", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which method is used to find the optimal solution in integer programming problems? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Simplex method", on_click=on_click1,),
             ft.TextButton(text="b) Branch and Bound ",on_click=on_click2),
             ft.TextButton(text="c) Linear regression",on_click=on_click1,),
             ft.TextButton(text="d) Transportation method", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Monte Carlo simulation is a technique used in Operations Research to: ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Solve linear programming problems", on_click=on_click1,),
             ft.TextButton(text="b) Analyze queuing systems",on_click=on_click1),
             ft.TextButton(text="c) Model uncertainty and risk in decision-making ",on_click=on_click2,),
             ft.TextButton(text="d) Optimize project schedules", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     



































































              #natural resources




              
        if page.route == "/es":
            page.views.append(
                ft.View(
                    "/es",
                    [
                        ft.AppBar(title=ft.Text("Environmental Science"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     






                   
        if page.route == "/cb":
            page.views.append(
                ft.View(
                    "/cb",
                    [
                        ft.AppBar(title=ft.Text("Conservation Biology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             

             


                        
        if page.route == "/srm":
            page.views.append(
                ft.View(
                    "/srm",
                    [
                        ft.AppBar(title=ft.Text("Sustainable Resource Management"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




            


                  

                        
        if page.route == "/epl":
            page.views.append(
                ft.View(
                    "/epl",
                    [
                        ft.AppBar(title=ft.Text("Environmental Policy and Law"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()







        if page.route == "/gis":
            page.views.append(
                ft.View(
                    "/gis",
                    [
                        ft.AppBar(title=ft.Text("Geographic Information Systems (GIS) and Remote Sensing"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()







              
        if page.route == "/nre":
            page.views.append(
                ft.View(
                    "/nre",
                    [
                        ft.AppBar(title=ft.Text("Natural Resource Economics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()







              



                
        if page.route == "/res":
            page.views.append(
                ft.View(
                    "/res",
                    [
                        ft.AppBar(title=ft.Text("Renewable Energy and Sustainability"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()







              

            
                
        if page.route == "/swrm":
            page.views.append(
                ft.View(
                    "/swrm",
                    [
                        ft.AppBar(title=ft.Text("Soil and Water Resources Management"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. What is the primary source of greenhouse gas emissions that contribute to climate change? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Methane emissions from livestock", on_click=on_click1,),
             ft.TextButton(text="b) Carbon dioxide (CO2) emissions from burning fossil fuels",on_click=on_click2),
             ft.TextButton(text="c) Nitrous oxide emissions from agricultural activities",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) from refrigerants", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  What is the process by which water evaporates from plant leaves into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click2,),
             ft.TextButton(text="b) Condensation",on_click=on_click1),
             ft.TextButton(text="c) Precipitation",on_click=on_click1,),
             ft.TextButton(text="d) Infiltration", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which layer of the Earth's atmosphere contains the ozone layer that protects us from harmful ultraviolet (UV) radiation? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Troposphere", on_click=on_click1,),
             ft.TextButton(text="b) Stratosphere",on_click=on_click2),
             ft.TextButton(text="c) Mesosphere",on_click=on_click1,),
             ft.TextButton(text="d) Thermosphere", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4. What is the term for the variety of life forms, including plants, animals, and microorganisms, found in an ecosystem?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Biodiversity ", on_click=on_click1,),
             ft.TextButton(text="b) Eutrophication",on_click=on_click2),
             ft.TextButton(text="c) Biomagnification",on_click=on_click1,),
             ft.TextButton(text="d) Ecotone", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5.Acid rain is caused by the release of which two pollutants into the atmosphere? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2) and sulfur dioxide (SO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx) and volatile organic compounds (VOCs)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2) and nitrogen oxides (NOx)",on_click=on_click2,),
             ft.TextButton(text="d) Carbon monoxide (CO) and particulate matter (PM)", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. Which process involves the conversion of nitrogen gas (N2) into forms that can be used by plants and organisms?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Transpiration", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen fixation",on_click=on_click2),
             ft.TextButton(text="c) Photosynthesis",on_click=on_click1,),
             ft.TextButton(text="d) Carbon sequestration", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. The accumulation of harmful substances in the tissues of organisms as they move up the food chain is known as:",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="a) Biomagnification", on_click=on_click2,),
             ft.TextButton(text="b) Bioaccumulation",on_click=on_click1),
             ft.TextButton(text="c) Biodiversity loss",on_click=on_click1,),
             ft.TextButton(text="d) Bioremediation", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is the term for the long-term changes in temperature and typical weather patterns in a place?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Climate", on_click=on_click2,),
             ft.TextButton(text="b) Weather",on_click=on_click1),
             ft.TextButton(text="c) Erosion",on_click=on_click1,),
             ft.TextButton(text="d) Biome", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9.The ozone layer is depleted by the release of which human-made chemicals? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Carbon dioxide (CO2)", on_click=on_click1,),
             ft.TextButton(text="b) Nitrogen oxides (NOx)",on_click=on_click1),
             ft.TextButton(text="c) Sulfur dioxide (SO2)",on_click=on_click1,),
             ft.TextButton(text="d) Chlorofluorocarbons (CFCs) ", on_click=on_click2,),
             ft.Text(""),



             

                          ft.Text("Questions 10.  Which international agreement aims to address global climate change by reducing greenhouse gas emissions?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="a) Kyoto Protocol", on_click=on_click1,),
             ft.TextButton(text="b) Paris Agreement",on_click=on_click2),
             ft.TextButton(text="c) Montreal Protocol",on_click=on_click1,),
             ft.TextButton(text="d) Stockholm Convention", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()






     


 
















































                #optometry



               
        if page.route == "/ap":
            page.views.append(
                ft.View(
                    "/ap",
                    [
                        ft.AppBar(title=ft.Text("Anatomy and Physiology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/ob":
            page.views.append(
                ft.View(
                    "/ob",
                    [
                        ft.AppBar(title=ft.Text("Ocular Biology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/opr":
            page.views.append(
                ft.View(
                    "/opr",
                    [
                        ft.AppBar(title=ft.Text("Optics and Refraction"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/vo":
            page.views.append(
                ft.View(
                    "/vo",
                    [
                         ft.AppBar(title=ft.Text("Visual Optics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/odp":
            page.views.append(
                ft.View(
                    "/odp",
                    [
                        ft.AppBar(title=ft.Text("Ocular Disease and Pathology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/bvvt":
            page.views.append(
                ft.View(
                    "/bvvt",
                    [
                        ft.AppBar(title=ft.Text("Binocular Vision and Vision Therapy"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/pha":
            page.views.append(
                ft.View(
                    "/pha",
                    [
                        ft.AppBar(title=ft.Text("Pharmacology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/pop":
            page.views.append(
                ft.View(
                    "/pop",
                    [
                        ft.AppBar(title=ft.Text("Pediatric Optometry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     

    








































































                 #physics

   
                
        if page.route == "/clm":
            page.views.append(
                ft.View(
                    "/clm",
                    [
                        ft.AppBar(title=ft.Text("Classical Mechanics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/elt":
            page.views.append(
                ft.View(
                    "/elt",
                    [
                        ft.AppBar(title=ft.Text("Electromagnetism"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/qum":
            page.views.append(
                ft.View(
                    "/qum",
                    [
                        ft.AppBar(title=ft.Text("Quantum Mechanics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/tsm":
            page.views.append(
                ft.View(
                    "/tsm",
                    [
                        ft.AppBar(title=ft.Text("Thermodynamics and Statistical Mechanics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/mop":
            page.views.append(
                ft.View(
                    "/mop",
                    [
                        ft.AppBar(title=ft.Text("Modern Physics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/ssp":
            page.views.append(
                ft.View(
                    "/ssp",
                    [
                        ft.AppBar(title=ft.Text("Solid State Physics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/fum":
            page.views.append(
                ft.View(
                    "/fum",
                    [
                        ft.AppBar(title=ft.Text("Fluid Mechanics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/opt":
            page.views.append(
                ft.View(
                    "/opt",
                    [
                        ft.AppBar(title=ft.Text("Optics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     















































               #mathematics


               
        if page.route == "/cal":
            page.views.append(
                ft.View(
                    "/cal",
                    [
                        ft.AppBar(title=ft.Text("Calculus"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/lig":
            page.views.append(
                ft.View(
                    "/lig",
                    [
                        ft.AppBar(title=ft.Text("Linear Algebra"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/dim":
            page.views.append(
                ft.View(
                    "/dim",
                    [
                        ft.AppBar(title=ft.Text("Discrete Mathematics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/pas":
            page.views.append(
                ft.View(
                    "/pas",
                    [
                        ft.AppBar(title=ft.Text("Probability and Statistics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),

 
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/nut":
            page.views.append(
                ft.View(
                    "/nut",
                    [
                        ft.AppBar(title=ft.Text("Number Theory"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/diq":
            page.views.append(
                ft.View(
                    "/diq",
                    [
                        ft.AppBar(title=ft.Text("Differential Equations"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/rea":
            page.views.append(
                ft.View(
                    "/rea",
                    [
                        ft.AppBar(title=ft.Text("Real Analysis"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/aba":
            page.views.append(
                ft.View(
                    "/aba",
                    [
                        ft.AppBar(title=ft.Text("Abstract Algebra"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     
















































                  #chemistry


                  
        if page.route == "/gec":
            page.views.append(
                ft.View(
                    "/gec",
                    [
                        ft.AppBar(title=ft.Text("General Chemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/ogc":
            page.views.append(
                ft.View(
                    "/ogc",
                    [
                        ft.AppBar(title=ft.Text("Organic Chemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/inc":
            page.views.append(
                ft.View(
                    "/inc",
                    [
                        ft.AppBar(title=ft.Text("Inorganic Chemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),

 
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/phc":
            page.views.append(
                ft.View(
                    "/phc",
                    [
                        ft.AppBar(title=ft.Text("Physical Chemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


           
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/anc":
            page.views.append(
                ft.View(
                    "/anc",
                    [
                        ft.AppBar(title=ft.Text("Analytical Chemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),

 
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
        
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/bic":
            page.views.append(
                ft.View(
                    "/bic",
                    [
                        ft.AppBar(title=ft.Text("Biochemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
          
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/enc":
            page.views.append(
                ft.View(
                    "/enc",
                    [
                        ft.AppBar(title=ft.Text("Environmental Chemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/coc":
            page.views.append(
                ft.View(
                    "/coc",
                    [
                        ft.AppBar(title=ft.Text("Computational Chemistry"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


          
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





































              #statistics


              
        if page.route == "/sin":
            page.views.append(
                ft.View(
                    "/sin",
                    [
                        ft.AppBar(title=ft.Text("Statistical Inference"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/ren":
            page.views.append(
                ft.View(
                    "/ren",
                    [
                        ft.AppBar(title=ft.Text("Regression Analysis"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                            
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/mus":
            page.views.append(
                ft.View(
                    "/mus",
                    [
                        ft.AppBar(title=ft.Text("Multivariate Statistics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


           ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/epd":
            page.views.append(
                ft.View(
                    "/epd",
                    [
                        ft.AppBar(title=ft.Text("Experimental Design"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),

ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/tsa":
            page.views.append(
                ft.View(
                    "/tsa",
                    [
                        ft.AppBar(title=ft.Text("Time Series Analysis"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                            
          
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/bas":
            page.views.append(
                ft.View(
                    "/bas",
                    [
                        ft.AppBar(title=ft.Text("Bayesian Statistics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     






                

        if page.route == "/nos":
            page.views.append(
                ft.View(
                    "/nos",
                    [
                        ft.AppBar(title=ft.Text("Nonparametric Statistics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
                 









                 

        if page.route == "/dmml":
            page.views.append(
                ft.View(
                    "/dmml",
                    [
                        ft.AppBar(title=ft.Text("Data Mining and Machine Learning"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     

















      












                   #biochemistry






                   
        if page.route == "/ceb":
            page.views.append(
                ft.View(
                    "/ceb",
                    [
                        ft.AppBar(title=ft.Text("Cell Biology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/mob":
            page.views.append(
                ft.View(
                    "/mob",
                    [
                        ft.AppBar(title=ft.Text("Molecular Biology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/enz":
            page.views.append(
                ft.View(
                    "/enz",
                    [
                        ft.AppBar(title=ft.Text("Enzymology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/met":
            page.views.append(
                ft.View(
                    "/met",
                    [
                        ft.AppBar(title=ft.Text("Metabolism"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/bit":
            page.views.append(
                ft.View(
                    "/bit",
                    [
                        ft.AppBar(title=ft.Text("Biochemical Techniques"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/psf":
            page.views.append(
                ft.View(
                    "/psf",
                    [
                        ft.AppBar(title=ft.Text("Protein Structure and Function"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
               
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/nua":
            page.views.append(
                ft.View(
                    "/nua",
                    [
                        ft.AppBar(title=ft.Text("Nucleic Acids"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/lmb":
            page.views.append(
                ft.View(
                    "/lmb",
                    [
                        ft.AppBar(title=ft.Text("Lipids and Membrane Biology"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


          
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     

























                        #arts



                        
        if page.route == "/das":
            page.views.append(
                ft.View(
                    "/das",
                    [
                        ft.AppBar(title=ft.Text("Drawing and Sketching"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/paint":
            page.views.append(
                ft.View(
                    "/paint",
                    [
                        ft.AppBar(title=ft.Text("Painting"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),

 ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/sup":
            page.views.append(
                ft.View(
                    "/sup",
                    [
                        ft.AppBar(title=ft.Text("Sculpture"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/photo":
            page.views.append(
                ft.View(
                    "/photo",
                    [
                        ft.AppBar(title=ft.Text("Photography"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/gad":
            page.views.append(
                ft.View(
                    "/gad",
                    [
                        ft.AppBar(title=ft.Text("Graphic Design"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),

 ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/dil":
            page.views.append(
                ft.View(
                    "/dil",
                    [
                        ft.AppBar(title=ft.Text("Digital Illustration"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/print":
            page.views.append(
                ft.View(
                    "/print",
                    [
                        ft.AppBar(title=ft.Text("Printmaking"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),

 ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
         
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/art":
            page.views.append(
                ft.View(
                    "/art",
                    [
                        ft.AppBar(title=ft.Text("Art History"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     








































                     #agric


                     
        if page.route == "/cos":
            page.views.append(
                ft.View(
                    "/cos",
                    [
                        ft.AppBar(title=ft.Text("Crop Science"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,horizontal_alignment=ft.CrossAxisAlignment.START,vertical_alignment=ft.MainAxisAlignment.START,
                )
            )
        page.update()
     




             


             

        if page.route == "/soil":
            page.views.append(
                ft.View(
                    "/soil",
                    [
                        ft.AppBar(title=ft.Text("Soil Science"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
              










              

        if page.route == "/aec":
            page.views.append(
                ft.View(
                    "/aec",
                    [
                        ft.AppBar(title=ft.Text("Agricultural Economics"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     









     

        if page.route == "/aerd":
            page.views.append(
                ft.View(
                    "/aerd",
                    [
                        ft.AppBar(title=ft.Text("Agricultural Extension and Rural Development"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     











     

        if page.route == "/sua":
            page.views.append(
                ft.View(
                    "/sua",
                    [
                        ft.AppBar(title=ft.Text("Sustainable Agriculture"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
           
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     




        if page.route == "/age":
            page.views.append(
                ft.View(
                    "/age",
                    [
                        ft.AppBar(title=ft.Text("Agricultural Engineering"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     





        if page.route == "/agm":
            page.views.append(
                ft.View(
                    "/agm",
                    [
                        ft.AppBar(title=ft.Text("Agribusiness Management"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


             
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
            
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     







        if page.route == "/ans":
            page.views.append(
                ft.View(
                    "/ans",
                    [
                        ft.AppBar(title=ft.Text("Animal Science"), bgcolor=ft.colors.BLUE_900),
                        ft.FloatingActionButton("Go back", on_click=lambda _: page.go("/quiz"), icon=ft.icons.ARROW_BACK_IOS,
                                                 bgcolor=ft.colors.BLUE_900,
                      
                                                 ),


            
            
            ft.Text("Questions 1. Which of the following is not a keyword in java?  ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Static", on_click=on_click2,),
             ft.TextButton(text="B - Boolean",on_click=on_click1),
             ft.TextButton(text="C - void",on_click=on_click1,),
             ft.TextButton(text="D - private", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 2.  what is the defaut value of INT variable ? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - 0", on_click=on_click1,),
             ft.TextButton(text="B - 0.0",on_click=on_click2),
             ft.TextButton(text="C - null",on_click=on_click1,),
             ft.TextButton(text="D - not defined", on_click=on_click1,),
             ft.Text(""),
                      
                         



                          ft.Text("Questions 3. Which of the following is true about public access modifier? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Variables, methods and constructors which are declared public can be accessed by any class.", on_click=on_click2,),
             ft.TextButton(text="B - Variables, methods and constructors which are declared public can be accessed by any class lying in same package.",on_click=on_click1),
             ft.TextButton(text="C - Variables, methods and constructors which are declared public in the superclass can be accessed only by its child class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                      
                         

                         

                          ft.Text("Questions 4.What is instance variable? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - Instance variables are static variables within a class but outside any method.", on_click=on_click1,),
             ft.TextButton(text="B - Instance variables are variables defined inside methods, constructors or blocks.",on_click=on_click2),
             ft.TextButton(text="C - Instance variables are variables within a class but outside any method.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 5. What is true about a final class?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - class declard final is a final class.", on_click=on_click1,),
             ft.TextButton(text="B - Final classes are created so the methods implemented by that class cannot be overridden.",on_click=on_click2),
             ft.TextButton(text="C - It can't be inherited.",on_click=on_click1,),
             ft.TextButton(text="D - All of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 6. What invokes a thread's run() method?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - JVM invokes the thread's run() method when the thread is initially executed.", on_click=on_click2,),
             ft.TextButton(text="B - Main application running the thread.",on_click=on_click1),
             ft.TextButton(text="C - start() method of the thread class.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



                      

                      

                          ft.Text("Questions 7. Question 7.  What is runtime polymorphism?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold",),
            ft.TextButton(text="A - Runtime polymorphism is a process in which a call to an overridden method is resolved at runtime rather than at compile-time.", on_click=on_click2,),
             ft.TextButton(text="B - Runtime polymorphism is a process in which a call to an overloaded method is resolved at runtime rather than at compile-time.",on_click=on_click1),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),




             

                          ft.Text("Questions 8. What is currentThread()?",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - It is a Thread public static method used to obtain a reference to the current thread.", on_click=on_click2,),
             ft.TextButton(text="B - It is a thread's instance method used to get thread count.",on_click=on_click1),
             ft.TextButton(text="C - It is a object's public static method used obtain a reference to the current thread.",on_click=on_click1,),
             ft.TextButton(text="D - It is a object's instance method used to get thread count.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 9. Which of the following is true about String? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - String is mutable.", on_click=on_click1,),
             ft.TextButton(text="B - String is immutable.",on_click=on_click2),
             ft.TextButton(text="C - String is a data type.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),



             

                          ft.Text("Questions 10. What is function overriding? ",color="white",style=ft.TextThemeStyle.LABEL_LARGE,weight="bold"),
            ft.TextButton(text="A - If a subclass uses a method that is already provided by its parent class, it is known as Method Overriding.", on_click=on_click1,),
             ft.TextButton(text="B - If a subclass provides a specific implementation of a method that is already provided by its parent class, it is known as Method Overriding.",on_click=on_click2),
             ft.TextButton(text="C - Both of the above.",on_click=on_click1,),
             ft.TextButton(text="D - None of the above.", on_click=on_click1,),
             ft.Text(""),
                                   
                    ],scroll=ft.ScrollMode.ALWAYS,bgcolor=ft.colors.BLUE_900,vertical_alignment=ft.MainAxisAlignment.START,horizontal_alignment=ft.CrossAxisAlignment.START,
                )
            )
        page.update()
     


















    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main, )