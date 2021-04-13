from styles import tier_colour

class KaggleStyles:
   
    def present(self,data):
        
        
        style = """<style>
                    @import url(https://fonts.googleapis.com/css2?family=Inter);
                    @keyframes currstreak {
                        0% { font-size: 3px; opacity: 0.2; }
                        80% { font-size: 34px; opacity: 1; }
                        100% { font-size: 28px; opacity: 1; }
                    }
                    @keyframes fadein {
                        0% { opacity: 0; }
                        100% { opacity: 1; }
                    }
                </style>"""
        
        
        return f"""

       


            <svg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' style='isolation:isolate' viewBox='0 0 495 195' width='495px' height='195px'>
                    {style}
                    <defs>
                        <clipPath id='_clipPath_OZGVUqgkTHHpPTYeqOmK3uLgktRVSwWw'>
                            <rect width='495' height='195'/>
                        </clipPath>
                    </defs>

               


                    <g xmlns="http://www.w3.org/2000/svg" style="isolation:isolate">
                        <path d="M 4.5 0 L 490.5 0 C 492.984 0 495 2.016 495 4.5 L 495 190.5 C 495 192.984 492.984 195 490.5 195 L 4.5 195 C 2.016 195 0 192.984 0 190.5 L 0 4.5 C 0 2.016 2.016 0 4.5 0 Z" style="stroke: #e4e2e2; fill: #fffefe;stroke-miterlimit:10;rx: 4.5;"/>
                    </g>
                    

                    <g xmlns="http://www.w3.org/2000/svg" transform="translate(1,48)">
                    
                    <text x="20" y="-12" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:700;font-size:22px;font-style:normal;fill:{tier_colour[data["performanceTier"]]};stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {data["displayName"]}
                    </text>

                     <text x="20" y="22" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:14px;font-style:normal;fill:#151515;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {"" if not data["occupation"] or not data["organization"] else data["occupation"]+" at " + data["organization"]}
                    </text>

                    <text x="20" y="40" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:14px;font-style:normal;fill:#151515;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        {"" if not data["country"] else data["country"]}{"" if not data["region"] else ", "+data["region"]}{"" if not data["city"] else ", " + data["city"]}.
                    </text>
                   

                   <text x="20" y="68" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:16px;font-style:normal;fill:#757678;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        Followers : {data["followers"]["count"]}
                    </text>
                    <text x="20" y="86" dominant-baseline="middle" stroke-width="0" style="font-family: Roboto, system-ui, sans-serif;font-weight:500;font-size:16px;font-style:normal;fill:#757678;stroke:none; opacity: 0; animation: fadein 0.5s linear forwards 0.6s;">
                        Following : {data["following"]["count"]}
                    </text>
                </g>

            <!--<g xmlns="http://www.w3.org/2000/svg" style="isolation:isolate" transform="scale(2.5)"><circle r="22.5" cx="24" cy="24" fill="url(#profileimg)" stroke-width="3" style="stroke: rgb(241, 243, 244);"/><path d="M 10.774831823419357 42.20288237343632 A 22.5 22.5 0 1 0 24 1.5" fill="none" style="stroke: rgb(101, 31, 255);" stroke-width="3"/></g>-->

                </svg>


            """


