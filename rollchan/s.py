# -*- coding: utf-8 -*-
from mintAPI import *
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
import time, json, codecs, re
import random, requests
import datetime

login = """
พิมพ์ /help เพื่อดูคำสั่งทั้งหมด


หากพบปัญหาระหว่างการใช้งาน โปรดติดต่อ Creator โดยเร็วค่ะ


โปรดปิด Letter Sealing ก่อนใช้งาน
line://nv/settings/privacy


หากไม่ได้ใช้งานแล้วโปรดไปที่ลิงก์ด้านล่างแล้วออกจากระบบค่ะ
line://nv/connectedDevices"""


APP = 'WIN10\t5.5.5\tShiro-NeNe\t11.3.4'
shi = LINE(appName=APP)
#shi.sendMessage("u68974d03060e115360852c149d37f000", f"{shi.profile.displayName} ล็อกอินเข้าสู่ระบบเสร็จสิ้น \n\nSelfBotName : 🌸RollChan🌸\nSelfBotType : บอททั่วไป/เกม\n"+login)
shi.sendMessage("u56fc52f1c41573793635b3b1bbca2405","กรุณากดยินยอมการใช้งานในลิงค์นี้\nline://app/1602687308-GXq4Vvk9")
print("Token : " + shi.authToken)
oepoll = OEPoll(shi)
clm = shi.profile.mid
settingsOpen = codecs.open("71.json","r","utf-8")
settings = json.load(settingsOpen)
now = datetime.datetime.now()
lineMID = shi.getProfile().mid

help1 = """###👤คำสั่งผู้ใช้งาน👤###
- /me ส่งคอนแท็คตัวเอง
- /myprofile ดูโปรไฟล์
- /status [ข้อความ] เปลี่ยนสเตตัส
- /name [ชื่อ] เปลี่ยนชื่อ
- /myname เช็คชื่อที่กำลังใช้งาน
- /mystatus เช็คสเตตัสที่กำลังใช้งาน"""

help2 = """###🔢คำสั่งตัวเลข🔢###
- /number [จำนวน] รันเลข
- /plus [จำนวน] [จำนวน] บวกเลข
- /minus [จำนวน] [จำนวน] ลบเลข
- /mul [จำนวน] [จำนวน] คูณเลข
- /div [จำนวน] [จำนวน] หารเลข
- /power [จำนวน] [เลขชี้กำลัง] หาค่าของเลขยกกำลัง"""

help3 = """##✍️คำสั่งแสดงข้อมูลต่างๆ✍️##
- /mid ส่ง mid ตัวเอง
- /gid ส่งไอดีกลุ่ม
- /getmid ส่ง mid คนอื่น (แชทส่วนตัว)
- /getcontact ส่งคอนแทคคนอื่น (แชทส่วนตัว)
- /whois [mid] ส่งคอนแทคจาก mid
- /gurl ส่งลิ้งก์กลุ่ม
- /contactmid ส่ง mid จากคอนแทค (พิมพ์คำสั่งนี้เพื่อดูวิธีใช้งาน)
- /posturl ส่งลิ้งก์โพสต์ (พิมพ์คำสั่งนี้เพื่อดูวิธีใช้งาน)
- /postid ส่ง Mid+ไอดีโพสต์(พิมพ์คำสั่งนี้เพื่อดูวิธีใช้งาน)"""

help4 = """###🎲คำสั่งเกมต่างๆ🎲###
- /rps เกมเป่ายิ้งฉุบ
- /coin โยนเหรียญ
- /dice ทอยลูกเต๋า
- /slot หมุนเครื่องสล็อตแมชชีน
- /roulette เกมรัสเซียนรูเล็ต
- /pokcard เกมป๊อกเด้ง
- /hilo เกมไฮโล"""

help5 = """###🌙คำสั่งอื่นๆ🌙###
- /ping เช็คการตอบสนองของบอท
- /pingV2 (Creator)
- /datetime ดูวันที่และเวลา
- /gift ส่งของขวัญ
- /speed ทดสอบความเร็ว
- /goodbye ออกจากกลุ่ม
- /uptime ดูระยะเวลาการใช้งาน
- /creator ส่งคอนแท็คผู้สร้าง"""

post = """🌸วิธีการใช้งาน🌸
1.แชร์โพสต์ลงแชท
2.พิมพ์คำสั่งลงแชทนั้น"""

card = ["ควีนโพธิ์ดำ♠️","2 โพธิ์แดง♥️","1 ข้าวหลามตัด♦️","4 ดอกจิก♣️","2 ข้าวหลามตัด♦️","ควีนโพธิ์แดง♥️","3 โพธิ์ดำ♠️","3 ข้าวหลามตัด♦️","คิงโพธิ์แดง♥️","4 โพธิ์ดำ♠️","4 ข้าวหลามตัด♦️","คิงโพธิ์ดำ♠️","5 โพธิ์ดำ♠️","3 ดอกจิก♣️","5 ดอกจิก♣️","9 โพธิ์ดำ♠️","10 โพธิ์แดง♥️","1 โพธิ์แดง♥️","1 ดอกจิก♣️","7 โพธิ์แดง♥️","2 ดอกจิก♣️","แจ็คโพธิ์แดง♥️","10 ข้าวหลามตัด♦️","10 ดอกจิก♣️","6 โพธิ์แดง♥️","ควีนข้าวหลามตัด♦️","6 ดอกจิก♣️","6 โพธิ์ดำ♠️","5 ข้าวหลามตัด♦️","9 ข้าวหลามตัด♦️","7 ดอกจิก♣️","ควีนดอกจิก♣️","7 โพธิ์ดำ♠️","คิงข้าวหลามตัด♦️","8 ข้าวหลามตัด♦️","8 โพธิ์ดำ♠️","9 โพธิ์แดง♥️","คิงดอกจิก♣️","8 ดอกจิก♣️","3 โพธิ์แดง♥️","1 โพธิ์ดำ♠️","4 โพธิ์แดง♥️","8 โพธิ์แดง♥️","7 ข้าวหลามตัด♦️","แจ็คข้าวหลามตัด♦️","แจ็คดอกจิก♣️","2 โพธิ์ดำ♠️","6 ข้าวหลามตัด♦️","9 ดอกจิก♣️","10 โพธิ์ดำ♠️","5 โพธิ์แดง♥️","แจ็คโพธิ์ดำ♠️"]

plus = """🌸วิธีการใช้งาน🌸

/plus [จำนวนเต็ม] [จำนวนเต็ม]

ตัวอย่าง : /plus 1 1

ผลลัพธ์ที่ได้ : 2"""

minus = """🌸วิธีการใช้งาน🌸

/minus [จำนวนเต็ม] [จำนวนเต็ม]

ตัวอย่าง : /minus 1 1

ผลลัพธ์ที่ได้ : 0"""

mul = """🌸วิธีการใช้งาน🌸

/mul [จำนวนเต็ม] [จำนวนเต็ม]

ตัวอย่าง : /mul 2 2

ผลลัพธ์ที่ได้ : 4"""

div = """🌸วิธีการใช้งาน🌸

/div [จำนวนเต็ม] [จำนวนเต็ม]

ตัวอย่าง : /div 2 2

ผลลัพธ์ที่ได้ : 1"""

power = """🌸วิธีการใช้งาน🌸

/power [จำนวนเต็ม] [จำนวนเต็ม]

ตัวอย่าง : /div 2 3

ผลลัพธ์ที่ได้ : 8"""

cm = """🌸วิธีการใช้งาน🌸
1.ส่งคอนแทค
2.พิมพ์คำสั่ง"""



rr = ["'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!","'ปัง!'\nทันใดนั้นเสียงปืนลูกโม่ก็ได้มีเสียงดังเกิดขึ้นและลูกกระสุนได้เข้าถึงหัวคุณเต็มๆ ทำให้คุณเสียชีวิต\nThe End","'แกร็ก..!'\nมันเป็นเพียงเสียงลั่นไกจากปืนลูกโม่ที่ไม่มีลูกกระสุนอยู่ดังนั้นคุณรอด!"]

creator = 'u68974d03060e115360852c149d37f000'

startTime = time.time()

autoblock = False

def sendflex(to, data):
    n1 = LiffChatContext(msg.to)
    n2 = LiffContext(chat=n1)
    view = LiffViewRequest('1602687308-GXq4Vvk9', n2)
    token = shi.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d เดือน" % (months)
    if weeks != 0: text += " %02d สัปดาห์" % (weeks)
    if days != 0: text += " %02d วัน" % (days)
    if hours !=  0: text +=  " %02d ชั่วโมง" % (hours)
    if mins != 0: text += " %02d นาที" % (mins)
    if secs != 0: text += " %02d วินาที" % (secs)
    if text[0] == " ":
            text = text[1:]
    return text
def status(op):
    global msg
    try:
        if op.type == 5:
          if settings["autoblock"] == True:
              shi.sendMessage(op.param1, "Auto Block!")
              shi.blockContact(op.param1)
          elif settings["autoblock"] == False:
              pass
        if op.type == 25:
            shi.log(f"{shi.profile.displayName} [25] SEND_MESSAGE")
            msg = op.message
            receiver = msg.to
            sender = msg._from
            text = msg.text
            if msg.text is None:
                return
            if msg.text.lower().startswith("/status "):
                    spl = msg.text.replace("/status ","")
                    i = shi.getProfile()
                    i.statusMessage = spl
                    shi.updateProfile(i)
                    shi.sendReplyMessage(msg.id, msg.to,"เปลี่ยนสเตตัสสำเร็จแล้วค่ะ(｀・ω・´)")
            elif msg.text.lower().startswith("/name "):
                spl = re.split("/name ",msg.text,flags=re.IGNORECASE)
                if spl[0] == "":
                  prof = shi.getProfile()
                  prof.displayName = spl[1]
                  shi.updateProfile(prof)
                  shi.sendReplyMessage(msg.id, msg.to, "เปลี่ยนชื่อสำเร็จแล้วค่ะ ( ´・ω・｀)")
            elif text.lower() == '/myname':
                shi.sendReplyMessage(msg.id, msg.to, '🌸ชื่อที่กำลังใช้งาน🌸 : \n' +shi.profile.displayName)
            elif text.lower() == '/mystatus':
                shi.sendReplyMessage(msg.id, msg.to, '🌸สเตตัสที่กำลังใช้งาน🌸 : \n' + shi.profile.statusMessage)
            elif text.lower() == '/mypic':
                me = shi.getContact(lineMID)
                me.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + shi.pictureStatus)
            elif text.lower() == '/mycover':
                me = shi.getContact(lineMID)
                cover = shi.getProfileCoverURL(lineMID)
                me.sendImageWithURL(msg.to, cover)
            elif text.lower() == '/gcreator':
                    group = shi.getGroup(msg.to)
                    GS = group.creator.mid
                    shi.sendContact(msg.to, GS)
            elif text.lower() == "/help":
                try:
                    contact = shi.getContact(msg._from)
                    zem={

  "type": "flex",
  "altText": "🌸ROLLCHANSENDFLEX🌸",
  "contents": {
    "type": "carousel",
    "contents": [
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://profile.line-scdn.net/" + contact.pictureStatus,
          "gravity": "center",
          "size": "full",
          "aspectRatio": "1:1",
          "aspectMode": "cover",
          "backgroundColor": "#EE12A1",
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "🌸RollChan Commands🌸",
              "size": "md",
              "align": "center",
              "weight": "bold",
              "color": "#000000",
            },
            {
              "type": "separator",
              "color": "#000000"
            },
            {

              "type": "text",
              "text": help1,
              "wrap": True,
              "margin": "md",
              "weight": "bold"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "spacer"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://profile.line-scdn.net/" + contact.pictureStatus,
          "gravity": "center",
          "size": "full",
          "aspectRatio": "1:1",
          "aspectMode": "cover",
          "backgroundColor": "#EE12A1",
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "🌸RollChan Commands🌸",
              "size": "md",
              "align": "center",
              "weight": "bold",
              "color": "#000000",
            },
            {
              "type": "separator",
              "color": "#000000"
            },
            {
              "type": "text",
              "text": help2,
              "wrap": True,
              "margin": "md",
              "weight": "bold"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "spacer"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://profile.line-scdn.net/" + contact.pictureStatus,
          "gravity": "center",
          "size": "full",
          "aspectRatio": "1:1",
          "aspectMode": "cover",
          "backgroundColor": "#EE12A1",
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "🌸RollChan Commands🌸",
              "size": "md",
              "align": "center",
              "weight": "bold",
              "color": "#000000",
            },
            {
              "type": "separator",
              "color": "#000000"
            },
            {
              "type": "text",
              "text": help3,
              "wrap": True,
              "margin": "md",
              "weight": "bold"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "spacer"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://profile.line-scdn.net/" + contact.pictureStatus,
          "gravity": "center",
          "size": "full",
          "aspectRatio": "1:1",
          "aspectMode": "cover",
          "backgroundColor": "#EE12A1",
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "🌸RollChan Commands🌸",
              "size": "md",
              "align": "center",
              "weight": "bold",
              "color": "#000000",
            },
            {
              "type": "separator",
              "color": "#000000"
            },
            {
              "type": "text",
              "text": help4,
              "wrap": True,
              "margin": "md",
              "weight": "bold"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "spacer"
            }
          ]
        }
      },
      {
        "type": "bubble",
        "hero": {
          "type": "image",
          "url": "https://profile.line-scdn.net/" + contact.pictureStatus,
          "gravity": "center",
          "size": "full",
          "aspectRatio": "1:1",
          "aspectMode": "cover",
          "backgroundColor": "#EE12A1",
        },
        "body": {
          "type": "box",
          "layout": "vertical",
          "contents": [
            {
              "type": "text",
              "text": "🌸RollChan Commands🌸",
              "size": "md",
              "align": "center",
              "weight": "bold",
              "color": "#000000",
            },
            {
              "type": "separator",
              "color": "#000000"
            },
            {
              "type": "text",
              "text": help5,
              "wrap": True,
              "margin": "md",
              "weight": "bold"
            }
          ]
        },
        "footer": {
          "type": "box",
          "layout": "vertical",
          "flex": 0,
          "spacing": "sm",
          "contents": [
            {
              "type": "spacer"
            }
          ]
        }
      }
    ]
  }
}
                sendflex(msg.to, zem)
                except:
                    shi.sendReplyMessage(msg.id, msg.to, help1+"\n"+help2+"\n"+help3+"\n"+help4+"\n"+help5)
            elif msg.text.lower().startswith("/number "):
                for i in range(int(msg.text.split(" ")[1])):
                    shi.sendMessage(msg.to, str(int(i+1)))
            elif text.lower().startswith("/flex "):
                contact = shi.getContact(msg._from)
                word = msg.text.replace("/flex ","")
                shi.unsendMessage(msg.id)
                flex={
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "body": {
      "type": "box",
      "layout": "horizontal",
      "margin": "xs",
      "contents": [
        {
          "type": "text",
          "text": word,
          "wrap": True,
          "flex": 10,
          "margin": "xs",
          "size": "sm",
          "align": "center",
          "gravity": "center",
          "weight": "bold",
          "color": "#EC4848"
        }
      ]
    },
    "styles": {
      "body": {
        "backgroundColor": "#000000",
        "separatorColor": "#382929"
      }
    }
  }
}
                try:
                    sendflex(msg.to, flex)
                except:
                    pass
            elif text.lower().startswith("/price "):
                ssr = msg.text.replace("/price ","")
                shi.unsendMessage(msg.id)
                doo={
  "type": "flex",
  "altText": "ใบเสร็จชำระเงิน",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "horizontal",
      "contents": [
        {
          "type": "text",
          "text": "ใบเสร็จ ชำระเงิน",
          "margin": "xxl",
          "size": "xl",
          "align": "center",
          "weight": "bold",
          "color": "#000000"
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": "https://www.234.in.th/images/2019/08/16/84E26FCC-43DF-4F78-8E4D-C0559310EDD9.jpg",
      "gravity": "center",
      "size": "full",
      "aspectRatio": "4:3",
      "aspectMode": "cover",
      "backgroundColor": "#FFFFFF",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com/"
      }
    },
    "body": {
      "type": "box",
      "layout": "horizontal",
      "spacing": "md",
      "contents": [
        {
          "type": "box",
          "layout": "vertical",
          "flex": 2,
          "contents": [
            {
              "type": "text",
              "text": "ราคารวมทั้งหมด "+ ssr +" บาท",
              "flex": 1,
              "size": "md",
              "gravity": "bottom",
              "weight": "bold",
              "color": "#000000"
            }
          ]
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "PayPal",
            "uri": "https://www.paypal.me/shironene"
          },
          "color": "#133978",
          "style": "primary"
        }
      ]
    },
    "styles": {
      "header": {
        "backgroundColor": "#FFFFFF"
      },
      "footer": {
        "backgroundColor": "#11EEE6"
      }
    }
  }
}
                sendflex(msg.to, doo)
            elif msg.text == "/shop":
                shi.unsendMessage(msg.id)
                ss={
  "type": "flex",
  "altText": "🌙ShiroNeko Shop🌙",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "header": {
      "type": "box",
      "layout": "vertical",
      "flex": 0,
      "contents": [
        {
          "type": "spacer",
          "size": "md"
        }
      ]
    },
    "hero": {
      "type": "image",
      "url": "https://www.234.in.th/images/2019/08/15/6409F443-48A1-4773-BF9B-CC2AC16B5FEB.jpg",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "backgroundColor": "#430505",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      }
    },
    "body": {
      "type": "box",
      "layout": "vertical",
      "spacing": "md",
      "action": {
        "type": "uri",
        "label": "Action",
        "uri": "https://linecorp.com"
      },
      "contents": [
        {
          "type": "text",
          "text": "ShiroNeko Shop",
          "size": "xl",
          "align": "center",
          "weight": "bold"
        },
        {
          "type": "separator",
          "color": "#000000"
        },
        {
          "type": "text",
          "text": "ขายสติ๊กเกอร์ ธีมไลน์จ้า",
          "size": "md",
          "align": "center",
          "weight": "bold"
        },
        {
          "type": "text",
          "text": "150 © = 40 ฿",
          "align": "center"
        },
        {
          "type": "text",
          "text": "10 © = 4 ฿",
          "align": "center"
        },
        {
          "type": "text",
          "text": "50 © = 14 ฿",
          "align": "center"
        },
        {
          "type": "text",
          "text": "100 © = 27 ฿",
          "align": "center"
        },
        {
          "type": "text",
          "text": "200 © = 54 ฿",
          "align": "center"
        },
        {
          "type": "text",
          "text": "250 © = 67 ฿ ",
          "align": "center"
        },
        {
          "type": "text",
          "text": "300 © = 81 ฿",
          "align": "center"
        },
        {
          "type": "text",
          "text": "🌙ซื้อมากกว่านี้สอบถามเข้ามาได้ค่า"
        },
        {
          "type": "text",
          "text": "🌙เหรียญแท้ทุกเรท 100%"
        },
        {
          "type": "text",
          "text": "🌙ขายจริงส่งจริงไม่มีโกง"
        },
        {
          "type": "separator",
          "color": "#000000"
        },
        {
          "type": "text",
          "text": "เปิดเช่าเซลฟ์บอทรายเดือน",
          "margin": "xl",
          "align": "center",
          "weight": "bold"
        },
        {
          "type": "text",
          "text": "ราคาเพียง 100฿ / เดือน",
          "align": "center"
        },
        {
          "type": "text",
          "text": "🌸ระบบบล็อคอัตโนมัติ"
        },
        {
          "type": "text",
          "text": "🌸ระบบจับอ่าน"
        },
        {
          "type": "text",
          "text": "🌸ระบบเช็คข้อความที่ยกเลิก"
        },
        {
          "type": "text",
          "text": "🌸ระบบรันเลข"
        },
        {
          "type": "text",
          "text": "🌸ระบบป้องกันแยกกลุ่ม"
        },
        {
          "type": "text",
          "text": "🌸ระบบล็อกอินอัตโนมัติ"
        },
        {
          "type": "text",
          "text": "และอื่นๆอีกมากมาย"
        },
        {
          "type": "separator",
          "color": "#000000"
        }
      ]
    },
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "spacer"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "สอบถาม/สั่งซื้อ",
            "uri": "line://ti/p/~nyssk"
          },
          "color": "#02B7FB",
          "style": "primary"
        }
      ]
    }
  }
}
                sendflex(msg.to, ss)
            elif msg.text == "/myprofile":
                contact = shi.getContact(msg._from)
                cover = shi.getProfileCoverURL(msg._from)
                shi.reissueUserTicket()
                res = "Myprofile Info\n"
                res += "Display Name :{}\n".format(contact.displayName)
                res += "Mid: {}\n".format(contact.mid)
                res += "Status Message\n"+"{}\n".format(contact.statusMessage)
                try:
                  poto = "https://os.line.naver.jp/os/p/{}".format(msg._from)
                except:
                  poto = "https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQcNdUbC8kEeVWqgR9qMX66lQ_hQPM8ScNY30x4nqpYaKY2jt02"
                dax = {
                  "type": "template",
                  "altText": "Myprofile",
                  "template": {
                    "type": "image_carousel",
                    "columns": [
                      {
                        "imageUrl": poto,
                        "layout": "horizontal",
                        "action": {
                          "type": "uri",
                          "label": "PROFILE",
                          "uri": poto,
                          "area": {
                            "x": 447,
                            "y": 356,
                            "width": 1040,
                            "height": 1040
                          }
                        }
                      },
                      {
                        "imageUrl": cover,
                        "layout": "horizontal",
                        "action": {
                          "type": "uri",
                          "label": "COVER",
                          "uri": cover,
                          "area": {
                            "x": 447,
                            "y": 356,
                            "width": 1040,
                            "height": 1040
                          }
                        }
                      },
                      {
                        "imageUrl": "https://qr-official.line.me/L/"+shi.getUserTicket().id+".png",
                        "layout": "horizontal",
                        "action": {
                          "type": "uri",
                          "label": "CONTACT",
                          "uri": "https://line.me/ti/p/"+shi.getUserTicket().id,
                          "area": {
                            "x": 447,
                            "y": 356,
                            "width": 1040,
                            "height": 1040
                          }
                        }
                      }
                    ]
                  }
                }
                sendflex(msg.to, dax)
            elif text.lower() == '/gurl':
                if msg.toType == 2:
                    shi.sendReplyMessage(msg.id, msg.to,"https://line.me/R/ti/g/"+str(shi.reissueGroupTicket(msg.to)))
                else:
                    shi.sendReplyMessage(msg.id, msg.to, "คำสั่งนี้ใช้ได้เฉพาะในกลุ่มเท่านั้นค่ะ")
            elif msg.text.lower().startswith("/creator"):
               try:
                   data={
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
    "type": "bubble",
    "direction": "ltr",
    "footer": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "spacer"
        },
        {
          "type": "button",
          "action": {
            "type": "uri",
            "label": "Contact Shiro",
            "uri": "line://ti/p/~nyssk"
          },
          "color": "#FD0077",
          "style": "primary"
        }
      ]
    }
  }
}
                   shi.sendContact(msg.to, creator)
                   shi.sendMessage(msg.to,"นี่คือคอนแทคผู้สร้างบอทค่ะ(*´ω｀*)")
                   sendflex(msg.to, data)
               except Exception as e:
                   pass
            elif msg.text.lower().startswith("/pingv2"):
                shi.sendReplyMessage(msg.id, msg.to, "Creator Only!")
            elif text.lower() == '/gid':
                    gid = shi.getGroup(msg.to)
                    shi.sendReplyMessage(msg.id, msg.to,gid.id)
            elif msg.text.lower().startswith("/whois "):
                men = msg.text.split(" ")
                get = msg.text.replace(men[0] + " ","")
                shi.sendContact(msg.to,str(get))
            elif text.lower() == "/mid":
                shi.sendReplyMessage(msg.id, msg.to, shi.profile.mid) 
            elif msg.text.lower().startswith("/ping"):
                shi.sendReplyMessage(msg.id, msg.to,"Pong!")
            elif msg.text.lower().startswith("/me"):
                shi.sendReplyMessage(msg.id,receiver, None, contentMetadata={'mid': sender}, contentType=13)
            elif text.lower() == '/datetime':
                now2 = datetime.datetime.now()
                nowY = datetime.datetime.strftime(now2,"%Y")
                nowB = datetime.datetime.strftime(now2,"%B")
                nowA = datetime.datetime.strftime(now2,"%A")
                nowD = datetime.datetime.strftime(now2,"%d")
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                nowC = datetime.datetime.strftime(now2,"%c")
                nowZ = datetime.datetime.strftime(now2,"%z")
                tm = "🌸เวลาและวันที่ปัจจุบัน🌸:\n\n"+"วัน : "+nowA+"\n"+"วันที่ : "+nowD+"\n"+"เดือน : "+nowB+"\n"+"ปี : "+nowY+"\n"+"เวลา : "+nowT+":"+nowM+":"+nowS+"\n"+"โซนเวลา : "+"(GMT+7) Bangkok"+"\n\n"+nowC
                shi.sendReplyMessage(msg.id, msg.to, tm)
            elif text.lower() == "/goodbye":
                shi.leaveGroup(msg.to)
            elif text.lower() == "/gift":
                shi.sendGift(msg.to,'jejejeeiiw9w99','sticker')
            elif msg.text.lower() == "/speed":
                start = time.time()
                shi.sendMessage(msg.to, "กำลังทดสอบความเร็วค่ะ")
                totalTime = time.time() - start
                shi.sendMessage(msg.to,format(str(totalTime)) + "วินาที")
            elif text.lower() == '/getmid':
                shi.sendReplyMessage(msg.id, msg.to,msg.to)
            elif text.lower() == '/getcontact':
                shi.sendContact(msg.to,msg.to)
            elif text.lower() == '/posturl':
                try:
                    shi.sendReplyMessage(msg.id, msg.to, shi.talk.getRecentMessagesV2(msg.to, 2)[1].contentMetadata["postEndUrl"])
                except:
                    shi.sendReplyMessage(msg.id, msg.to, post)
            elif text.lower() == '/postid':
                try:
                    shi.sendReplyMessage(msg.id, msg.to, shi.talk.getRecentMessagesV2(msg.to, 2)[1].contentMetadata["postEndUrl"].split("userMid=")[1])
                except:
                    shi.sendReplyMessage(msg.id, msg.to, post)
            elif text.lower() == '/uptime':
                timenow = time.time()
                runtime = timenow - startTime
                runtime = timeChange(runtime)
                shi.sendReplyMessage(msg.id, msg.to, "ระยะการทำงานของโรลจัง\n" + str(runtime))
            elif text.lower() == '/rps':
                s = random.choice(["ค้อน","กระดาษ","กรรไกร","ค้อน","กระดาษ","กรรไกร"])
                shi.sendReplyMessage(msg.id, msg.to,"ผลการเป่ายิ้งฉุบ : "+ s)
            elif text.lower() == '/coin':
                n = random.choice(["หัว","ก้อย","หัว","ก้อย"])
                shi.sendReplyMessage(msg.id, msg.to,"คุณกำลังโยนเหรียญ. . .")
                shi.sendMessage(msg.to,"ผลการโยนเหรียญ : "+ n)
            elif text.lower() == '/slot':
                s = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                t = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                r = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                v = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                a = random.choice('🍇🍇🍋🍑🍒⑦🍇🍋🍑🍒🍋🍑🍒🍑🍒🍒⑦🍋🍑🍒')
                shi.sendReplyMessage(msg.id, msg.to,"คุณกำลังหมุนเครื่องสล็อตแมชชีน. . .")
                shi.sendMessage(msg.to,"ผลเครื่องสล็อตแมชชีน :\n"+" | "+s+" | "+t+" | "+r+" | "+v+" | "+a+" | ")
            elif text.lower() == '/roulette':
                s = random.choice(rr)
                shi.sendReplyMessage(msg.id, msg.to, "คุณได้ทำการลั่นไกไปที่ปืนลูกโม่ปรากฎว่า...")
                shi.sendMessage(msg.to, s)
            elif text.lower() == '/dice':
                f = random.choice('123456')
                shi.sendReplyMessage(msg.id, msg.to,"คุณกำลังทอยลูกเต๋าอยู่. . .")
                shi.sendMessage(msg.to,"ผลการทอยลูกเต๋า : "+f+" แต้ม")
            elif text.lower() == '/hilo':
                f = random.choice('123456')
                r = random.choice('123456')
                t = random.choice('123456')
                d = int(f) + int(r) + int(t)
                shi.sendReplyMessage(msg.id, msg.to, "คุณกำลังทอยลูกเต๋าทั้ง3ลูก. . .")
                shi.sendMessage(msg.to, "🎲ผลการทอยทั้งหมด🎲\n\n"+"ลูกที่ 1 : "+f+" แต้ม"+"\n"+"ลูกที่ 2 : "+r+" แต้ม"+"\n"+"ลูกที่ 3 : "+t+" แต้ม"+"\n\n"+"แต้มรวมทั้งหมด "+str(d)+" แต้ม")
            elif text.lower() == '/pokcard':
                shi.sendMessage(msg.to, "ไพ่ที่คุณได้รับหลังจากการสับ :\n\n"+random.choice(card)+"\n"+random.choice(card)+"\n\nพิมพ์ /draw เพื่อจั่วไพ่")
            elif text.lower() == '/draw':
                shi.sendMessage(msg.to,"ไพ่ที่คุณได้รับหลังการจั่ว : \n\n"+random.choice(card))
            elif text.lower() == '/contactmid':
                try:
                    shi.sendReplyMessage(msg.id, msg.to, shi.talk.getRecentMessagesV2(msg.to, 2)[1].contentMetadata["mid"])
                except:
                    shi.sendMessage(msg.to, cm)
            elif text.lower() == '/picall':
                if msg.toType == 2:
                    gs = shi.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                       targets.append(g.mid)
                    if targets == []:
                      shi.sendReplyMessage(msg.id, msg.to,"สั่งได้เฉพาะในกลุ่มเท่านั้นนะค่ะ^_^")
                    else:
                        for target in targets:
                            try:
                                profile = shi.getContact(target)
                                shi.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+profile.pictureStatus)
                            except:
                                pass
            elif msg.text.lower() == '/autoblock on':
                    if settings["autoblock"] == True:
                        if settings["lang"] == "JP":
                            shi.sendReplyMessage(msg.id, msg.to, "เปิดโหมดบล็อกอัตโนมัติอยู่แล้วค่ะ")
                    else:
                        settings["autoblock"] = True
                        if settings["lang"] == "JP":
                            shi.sendReplyMessage(msg.id, msg.to, "เปิดโหมดบล็อกอัตโนมัติแล้วค่ะ")
            elif msg.text.lower() == '/autoblock off':
                    if settings["autoblock"] == False:
                        if settings["lang"] == "JP":
                            shi.sendReplyMessage(msg.id, msg.to, "ปิดโหมดบล็อกอัตโนมัติอยู่แล้วค่ะ")
                    else:
                        settings["autoblock"] = False
                        if settings["lang"] == "JP":
                            shi.sendReplyMessage(msg.id, msg.to, "ปิดโหมดบล็อกอัตโนมัติแล้วค่ะ")
            elif msg.text.lower().startswith("/power "):
                 try:
                     m = msg.text.split(" ")[1]
                     i = msg.text.split(" ")[2]
                     g = int(m) ** int(i)
                     shi.sendMessage(msg.to, str(g))
                 except:
                        shi.sendReplyMessage(msg.id, msg.to, power)
            elif msg.text.lower().startswith("/plus "):
                 try:
                     a = msg.text.split(" ")[1]
                     b = msg.text.split(" ")[2]
                     c = int(a) + int(b)
                     shi.sendMessage(msg.to, str(c))
                 except:
                        shi.sendReplyMessage(msg.id, msg.to, plus)
            elif msg.text.lower().startswith("/minus "):
                 try:
                     d = msg.text.split(" ")[1]
                     e = msg.text.split(" ")[2]
                     f = int(d) - int(e)
                     shi.sendMessage(msg.to, str(f))
                 except:
                        shi.sendReplyMessage(msg.id, msg.to, minus)
            elif msg.text.lower().startswith("/mul "):
                 try:
                     x = msg.text.split(" ")[1]
                     y = msg.text.split(" ")[2]
                     z = int(x) * int(y)
                     shi.sendMessage(msg.to, str(z))
                 except:
                        shi.sendReplyMessage(msg.id, msg.to, mul)
            elif msg.text.lower().startswith("/div "):
                 try:
                     q = msg.text.split(" ")[1]
                     p = msg.text.split(" ")[2]
                     m = int(q) / int(p)
                     shi.sendMessage(msg.to, str(m))
                 except:
                        shi.sendReplyMessage(msg.id, msg.to, div)
        if op.type == 26 and op.message._from == creator and op.message.toType == 2 and "/pingV2" in op.message.text:
            msg = op.message
            if msg.text is None:
               return
            try:
                shi.sendReplyMessage(msg.id, msg.to, "Pong! ( ´・ω・｀)")
            except Exception as e:
                pass
    except Exception as e:
         print(e)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                status(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        print(e)
