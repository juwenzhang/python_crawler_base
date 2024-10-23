from lxml import etree

html_doc = """
            <div class="directory-boxshadow-dialog" style="display:none;">
              <div class="directory-boxshadow-dialog-box">
              </div>
               <div class="vip-limited-time-offer-box-new" id="vip-limited-time-offer-box-new">
                  <img class="limited-img limited-img-new" src="https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-newWhite.png">
                  <div class="vip-limited-time-top">
                    确定要放弃本次机会？
                  </div>
                  <span class="vip-limited-time-text">福利倒计时</span>
                  <div class="limited-time-box-new">
                    <span class="time-hour"></span>
                    <i>:</i>
                    <span class="time-minite"></span>
                    <i>:</i>
                    <span class="time-second"></span>
                  </div>
                  <div class="limited-time-vip-box">
                    <p>
                      <img class="coupon-img" src="https://csdnimg.cn/release/blogv2/dist/pc/img/vip-limited-close-roup.png">
                      <span class="def">立减 ¥</span>
                      <span class="active limited-num"></span>
                    </p>
                    <span class="">普通VIP年卡可用</span>
                  </div>
                  <a class="limited-time-btn-new" href="https://mall.csdn.net/vip" data-report-click="{&quot;spm&quot;:&quot;1001.2101.3001.9621&quot;}" data-report-query="spm=1001.2101.3001.9621">立即使用</a>
              </div>
            </div>
           """

xml_doc = etree.HTML(html_doc)

# 开始实现查看我们的HTML的文档
# print(etree.tostring(xml_doc).decode())

res = xml_doc.xpath('//span/text()')
for i in res:
    print(i)

for i in xml_doc.xpath('//img/@src'):
    print(i)

for i in xml_doc.xpath('//a[@class="limited-time-btn-new"]/@href'):
    print(i)