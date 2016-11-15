网页正文内容抽取
===================

将原代码库从Python2升级为Python3版本，修复少量bug。


### 使用：
#### 先安装beautiful soup和html5lib

```bash
pip install beautifulsoup4
pip install html5lib
```

#### 然后把htm_body_extractor和extract_utils两个文件放入程序文件夹，仿照下面的代码开始使用
```python

    from html_body_extractor import BodyExtractor
    url = 'http://md.tech-ex.com/ired/2016/47848.html'
    te = BodyExtractor(url)
    te.execute()
    print(te.body)
    
```

### 输出：
```
Dan Cook(丹·库克)第一次开始探索脑电波技术的商业潜能是在20年前，他与对开发更高级测谎仪感兴趣的政府机构，以及希望了解药物对神经功能影响的制药公司合作。　　1993年，由于一部好莱坞的新派电影《The Lawnmower Man》(《割草者》)中所描绘的反乌托邦未来主义，VR成了古怪极客们的业余爱好。但是Cook希望能开发动画真人形象，直接由大脑发出的信号主导，并将他在加州大学伯克利分校认知神经科学专业研究生的作品向商业领域推广。 随着VR逐渐成为主流，Cook认为现在是脑波分析技术证明其价值的时候了。他的公司EyeMynd希望建立一套将脑电波转化为VR世界中的行为的操作系统。没有头显，没有控制器——只有思想，引导使用者穿越虚拟世界。　　“十年以后，这一切都会变得平淡无奇，”Cook说。他对自己的发明有着极度的真诚与热忱。“电脑的运行速度如此之快，以至于我们可以实时探测和分析所有的大脑信号……我们知道如何获取大脑向身体发出的所有信号与所有的感官信息，并进行全方位地认知与情感追踪。”　　EyeMynd公司设立在盐湖城与旧金山，Cook的兄弟Nate(精神心理学硕士)与David Traub(大卫·特劳布)(《割草者》的VR顾问)是公司的执行制作人。EyeMynd计划于2017年春天发布一款使用16个脑电图(EEG)传感器进行脑电波监测的头显。Developer Brainwave VR头显将与HTC Vive兼容，利用EyeMynd的Brainwave OS操作系统将头显读取的脑电图转化为电脑指令。 该款头显的初代版本将面向开发者，为他们提供使用脑电波分析能力设计应用的工具包。Cook无法给出其具体价格或发布日期，但表示这将是目前市面上同类设备中最舒适的一款。　　与头显共同发布的还有一款简单的游戏《Smile with Lucy》，作为个性化的大脑校准辅助。Cook表示，过去的校准过程需要一个小时，但是很快将发展到只需几分钟。在这一游戏中，玩家模仿电脑化身的面部表情，而EyeMynd软件监控玩家独特的脑电波模式——当我们看见、感觉、触摸或移动某物时产生的“模式识别”信号。 EyeMynd希望能够借助对VR配件不断增长的消费兴趣为自家产品造势。但是Cook认为，十年以后的标准电脑界面将只需要大脑传感器，如今使用的VR配件，包括运动传感器、手柄、头戴式加速器和摄像机都将不复存在。　　“理解脑电波操作系统的关键是思考梦境。在梦里，你不需要移动双腿就能跑步。梦境与想象制造出我们可以读取的大脑信号。对于我们想做的事，我们不需要眼睛看到、耳朵听到或是双手触到。这些都可以忽略。”　　在将基于脑电波的技术推向市场的探索中，EyeMynd并非独自一人。Emotiv和NeuroSky等公司已经为了科学应用的需要发布了EEG头显。其它公司则正在追求市场营销与广告应用，有些分析公司已经将VR传感器的数据分析作为追踪广告效应的方式。直接跟踪使用者潜意识中的肢体与情绪反应将成为广告界的“终极目标”，如果它能被实现的话。　　“VR内容提供者与这一新领域的开发者，没有可靠的方式确认他们是否与使用者建立了联系，”yotta.io公司的Charles Miller(查尔斯·米勒)表示。这家位于新奥尔良的公司也正开发脑电波传感器。“我们非常关注市场空间——提供真实可靠的数据与量化的指标。”　　然而，Cook和他的团队希望将脑电波技术应用于医疗和教育领域。但是，对于未来脑电波技术的商业应用，不论是在哪个领域，仍存在很多质疑。大多数神经系统科学家表示，大脑的电信号在实验室中可以比较精确地被“读取”，但是只有在经过某种程度的开刀手术的情况下。 “从概念上讲，这一点并不重要，但是几乎无法实现，”加州大学伯克利分校的Gallant Neuroscience Lab(格朗特神经系统科学实验室)主任Jack Gallant(杰克·格朗特)说。他表示，这一过程还包括大量的运算能力，并且在时间和金钱方面都过于昂贵。“从大脑外部破解EEG信号的问题在于颅骨是可恶的过滤器。根据我的经历，这是非常难跨越的障碍。”　　然而，Dan Cook不会让怀疑论阻挡他长达20年的追求。2016年，他花费了大部分时间筹集资金，建立合作关系，并计划于2017年在中国建立分公司，在春季将第一批头显运到开发者手中。　　Cook还补充道，Facebook的首席执行官Mark Zuckerberg(马克·扎克伯格)已经公开宣布了他对于脑对脑直接交流的设想。“Zuckerberg明白这就是未来，但我认为他还不了解我们距离实现这一设想是多么近在咫尺。他认为还需要几年的时间，而我们要在数月后实现。”　　VR模拟，Cook表示，只是人类发现我们所有经历都是可模拟的开始。计算机科学家们的幻想，即将成为在高新技术产业重要人物中流行的理论，包括Tesla(特斯拉)的首席执行官Elon Musk(伊隆·马斯克)。　　“我们处在大脑主导的模拟之中的模拟，即第二层模拟状态，”Cook说。“这在未来将变得平淡无奇。没有高于我们的创造者，但是我们却假装处在这受到疾病与痛苦困扰的愚蠢的肉体凡胎中。”　　“VR使我们可以巧妙地制造幻觉，以追求和享受全然独特的人类体验，”他说。“这为人类创造了一个充分了解自己的机会。”
```

### TODO：
- [ ] 保留段落结构，包括换行，分段等。
- [ ] 可输出样式与标签
- [ ] 进一步改进提取正确率