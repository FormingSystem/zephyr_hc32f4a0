---
id: learning.zephyr-docs.boards-shields.page-163
title: Seeed Studio COB LED Driver Board for XIAO
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/seeed_xiao_cob_led/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="seeed-studio-cob-led-driver-board-for-xiao"></a>

<a id="seeed-xiao-cob-led"></a>

# 第163章\_Seeed Studio XIAO COB LED驱动板（Driver Board）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/seeed_xiao_cob_led/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

<a id="id4"></a>

Seeed Studio XIAO COB LED驱动板[注1](#id3)是面向Seeed Studio XIAO系列的七通道照明载板，D0及D1提供2路大功率开关输出，D2、D3、D8及D9提供4路低有效PWM输出，用于调光效果。（[Seeed Studio XIAO COB LED驱动板（Driver Board）](https://wiki.seeedstudio.com/getting_started_with_cob_led_dirver_board/)）

在Zephyr中，此扩展板提供D0及D1上始终可用的2路GPIO开关输出，以及D2、D3、D8及D9上的4路可选PWM输出。基础设备树覆盖文件始终将D0及D1输出公开为led0及led1。扩展板描述了PWM输出，但在板级或应用覆盖文件将其连接到所接XIAO开发板的PWM硬件之前，这些输出保持禁用。

<a id="id2"></a>

![官方原图：Seeed Studio COB LED Driver Board for XIAO](images/seeed_xiao_cob_led.webp)

Seeed Studio XIAO COB LED驱动板，图片来源：Seeed Studio

<a id="pin-assignments"></a>

### 引脚分配（Pin Assignments）

<table>
<tr>
<th>XIAO引脚</th>
<th>Zephyr别名</th>
<th>功能（Function）</th>
</tr>
<tr>
<td>D0</td>
<td><code>led0</code></td>
<td>大功率开关输出0</td>
</tr>
<tr>
<td>D1</td>
<td><code>led1</code></td>
<td>大功率开关输出1</td>
</tr>
<tr>
<td>D2</td>
<td><code>pwm-led0</code></td>
<td>小功率PWM输出0，低有效</td>
</tr>
<tr>
<td><code>D3</code></td>
<td><code>pwm-led1</code></td>
<td>小功率PWM输出1，低有效</td>
</tr>
<tr>
<td>D8</td>
<td><code>pwm-led2</code></td>
<td>小功率PWM输出2，低有效</td>
</tr>
<tr>
<td>D9</td>
<td><code>pwm-led3</code></td>
<td>小功率PWM输出3，低有效</td>
</tr>
<tr>
<td>数据SDA／时钟SCL</td>
<td>不适用（N/A）</td>
<td>Grove I2C连接器</td>
</tr>
</table>

<a id="requirements"></a>

## 前置要求（Requirements）

此扩展板可用于提供XIAO连接器标签xiao_d的开发板。

扩展板定义始终为D0及D1的2路大功率输出提供GPIO LED别名。

D2、D3、D8及D9的4路小功率输出需要按所接XIAO开发板配置PWM路由。扩展板为这些输出定义pwm-led0至pwm-led3别名，但在板级或应用覆盖文件提供PWM控制器、通道及pinctrl配置之前，相应节点保持禁用。下节说明配置方法。

<a id="pwm-configuration"></a>

### PWM配置（PWM Configuration）

在指定引脚启用PWM需要开发板专用的PWM外设配置，因此必须为XIAO开发板提供类似[boards/shields/seeed_xiao_cob_led/boards/xiao_esp32c6_esp32c6_hpcore.overlay](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/shields/seeed_xiao_cob_led/boards/xiao_esp32c6_esp32c6_hpcore.overlay)的覆盖文件，可随本扩展板提供为板级覆盖文件，也可由应用提供。该文件应：


- 启用具有4个通道的PWM控制器，并配置适当的引脚控制，将其分配到扩展板D2、D3、D8及D9；
- 为扩展板pwm-led0至pwm-led3节点添加pwms属性。

此扩展板的小功率输出采用低有效逻辑，因此每个pwms条目均须设置PWM_POLARITY_INVERTED。

<a id="programming"></a>

## 编程（Programming）

调用west build时设置--shield seeed_xiao_cob_led。

例如，用[Blinky](../getting_started/P004_LED闪烁示例.md#blinky)示例控制大功率D0输出：

```text
# From the root of the zephyr repository
west build -b xiao_esp32c6/esp32c6/hpcore --shield seeed_xiao_cob_led samples/basic/blinky
```

再次提醒，使用PWM输出必须在设备树覆盖文件中提供PWM路由配置。随附的xiao_esp32c6/esp32c6/hpcore扩展板覆盖文件支持按以下方式构建[PWM Blinky](../basic_samples/P004_PWM闪烁LED.md#pwm-blinky)示例：

```text
# From the root of the zephyr repository
west build -b xiao_esp32c6/esp32c6/hpcore --shield seeed_xiao_cob_led samples/basic/blinky_pwm
```

<a id="references"></a>

## 参考资料（References）

<a id="id3"></a>

〔[1](#id4)〕 [https://wiki.seeedstudio.com/getting_started_with_cob_led_dirver_board/](https://wiki.seeedstudio.com/getting_started_with_cob_led_dirver_board/)

## 译注

官方概述称七通道，但列出的Zephyr输出为2路GPIO与4路PWM；PWM须有板级或应用覆盖配置才启用。

---

[上一章](P162_Seeed_W5500_Ethernet_Shield.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P164_Seeed_Studio_XIAO_Expansion_Board.md)
