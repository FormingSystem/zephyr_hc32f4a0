---
id: learning.zephyr-docs.dt-bus-binding-reference.page-1
title: GPIO绑定常量头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2gpio_2gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_GPIO绑定常量头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/dt-bindings_2gpio_2gpio_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)选择GPIO、SPI绑定常量或设备树宏工具包装头文件，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga335bf7efee07e03961ab91a86295897a"></a>

```c
#define GPIO_DT_FLAGS_MASK 0x7F
```

相关声明：[GPIO_DT_FLAGS_MASK](../hardware/P266_GPIO公共接口.md#ga335bf7efee07e03961ab91a86295897a)。

设备树 GPIO 标志的掩码（Mask）。

<a id="r_ga644109ce84c8feffe1226b9b50122a96"></a>

```c
#define GPIO_INT_WAKEUP (1 << 6)
```

相关声明：[GPIO_INT_WAKEUP](../hardware/P266_GPIO公共接口.md#ga644109ce84c8feffe1226b9b50122a96)。

配置 GPIO 中断，使其能够从低功耗模式（Low Power Mode）唤醒系统。

<a id="define-members-0"></a>

### GPIO引脚有效电平标志（Active Level Flags）

<a id="r_ga62cea8989df2425e5e5e712217d65f46"></a>

```c
#define GPIO_ACTIVE_LOW (1 << 0)
```

相关声明：[GPIO_ACTIVE_LOW](../hardware/P266_GPIO公共接口.md#ga62cea8989df2425e5e5e712217d65f46)。

GPIO 引脚处于低电平时为有效状态，即逻辑值为“1”。

<a id="r_gad93badd2828d065e7fd14cf40dd05039"></a>

```c
#define GPIO_ACTIVE_HIGH (0 << 0)
```

相关声明：[GPIO_ACTIVE_HIGH](../hardware/P266_GPIO公共接口.md#gad93badd2828d065e7fd14cf40dd05039)。

GPIO 引脚处于高电平时为有效状态，即逻辑值为“1”。

<a id="define-members-1"></a>

### GPIO引脚驱动标志（Drive Flags）

<a id="r_ga72b7ac5b3613d972b88268bee9068e35"></a>

```c
#define GPIO_OPEN_DRAIN (GPIO_SINGLE_ENDED | GPIO_LINE_OPEN_DRAIN)
```

相关声明：[GPIO_OPEN_DRAIN](../hardware/P266_GPIO公共接口.md#ga72b7ac5b3613d972b88268bee9068e35)。

将 GPIO 输出配置为开漏模式（Open Drain），即线与（Wired AND）。

<a id="r_ga5ace024873272a3f6727fc186afa0320"></a>

```c
#define GPIO_OPEN_SOURCE (GPIO_SINGLE_ENDED | GPIO_LINE_OPEN_SOURCE)
```

相关声明：[GPIO_OPEN_SOURCE](../hardware/P266_GPIO公共接口.md#ga5ace024873272a3f6727fc186afa0320)。

将 GPIO 输出配置为开源极模式（Open Source），即线或（Wired OR）。

<a id="define-members-2"></a>

### GPIO引脚偏置标志（Bias Flags）

<a id="r_gaaa7921da231fd2b96575fa522e2c1970"></a>

```c
#define GPIO_PULL_UP (1 << 4)
```

相关声明：[GPIO_PULL_UP](../hardware/P266_GPIO公共接口.md#gaaa7921da231fd2b96575fa522e2c1970)。

启用 GPIO 引脚上拉（Pull-up）。

<a id="r_gadec1802e074f3021d464da09cd66c7cf"></a>

```c
#define GPIO_PULL_DOWN (1 << 5)
```

相关声明：[GPIO_PULL_DOWN](../hardware/P266_GPIO公共接口.md#gadec1802e074f3021d464da09cd66c7cf)。

启用 GPIO 引脚下拉（Pull-down）。

## 1.2\_源码定位与版本边界

相对源码定位：[GPIO绑定常量](../../../include/zephyr/dt-bindings/gpio/gpio.h)、[SPI绑定常量](../../../include/zephyr/dt-bindings/spi/spi.h)、[设备树宏工具包装](../../../include/zephyr/dt-bindings/dt-util.h)、[GPIO驱动接口](../../../include/zephyr/drivers/gpio.h)、[SPI驱动接口](../../../include/zephyr/drivers/spi.h)、[基础宏工具](../../../include/zephyr/sys/util_macro.h)、[GPIO控制器绑定](../../../dts/bindings/gpio/gpio-controller.yaml)和[SPI设备绑定](../../../dts/bindings/spi/spi-device.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：有效电平与物理电平：GPIO_ACTIVE_LOW设定位0，GPIO_ACTIVE_HIGH为0；它们约定逻辑有效状态，不直接设定输出电压，也不包含输入／输出方向。逻辑读写接口考虑ACTIVE_LOW，带raw后缀的物理电平接口忽略这一逻辑反转；方向、输出初始化与中断触发模式另由驱动接口配置。

> 译注——源码核对：驱动与偏置：GPIO_OPEN_DRAIN组合单端驱动位1与开漏选择位2，GPIO_OPEN_SOURCE组合单端驱动位1与取值为0的开源极选择位2。开源极（Open Source）在这里是相对于开漏的输出模式名称，不是开放源代码。上拉、下拉分别占位4、位5；当前GPIO公共配置实现含有不能同时启用二者的断言，断言是否保留取决于构建配置，不能将其理解为各驱动始终返回统一错误。

> 译注——源码核对：标志布局与唤醒：GPIO_DT_FLAGS_MASK为0x7F，覆盖位0至6；源码另将位8至15保留给SoC专用标志，这个掩码不包含全部厂商位。GPIO_INT_WAKEUP占位6；gpio_pin_interrupt_configure_dt仅从设备树标志中合入该唤醒位，其他设备树标志在该中断配置路径被忽略。常量本身不保证控制器支持唤醒，也不替代中断使能与电源管理配置。

> 译注——源码核对：版本边界：本批记录三个绑定头文件、GPIO与SPI驱动公共头文件、宏工具头文件和两个公共绑定，共八份官方源码摘要；三个源码浏览页的非注释内容与读取的原始头文件一致。latest、滚动main与仓库参照版本不自动相同。相对链接用于源码跟踪，本次未生成设备树、构建固件或操作硬件。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 1.3\_原页交叉引用（Cross References）

- [查看此文件的源码](P002_GPIO绑定常量头文件源码.md)
- [GPIO_DT_FLAGS_MASK](../hardware/P266_GPIO公共接口.md#ga335bf7efee07e03961ab91a86295897a)
- [GPIO_INT_WAKEUP](../hardware/P266_GPIO公共接口.md#ga644109ce84c8feffe1226b9b50122a96)
- [GPIO_ACTIVE_LOW](../hardware/P266_GPIO公共接口.md#ga62cea8989df2425e5e5e712217d65f46)
- [GPIO_ACTIVE_HIGH](../hardware/P266_GPIO公共接口.md#gad93badd2828d065e7fd14cf40dd05039)
- [GPIO_OPEN_DRAIN](../hardware/P266_GPIO公共接口.md#ga72b7ac5b3613d972b88268bee9068e35)
- [GPIO_OPEN_SOURCE](../hardware/P266_GPIO公共接口.md#ga5ace024873272a3f6727fc186afa0320)
- [GPIO_PULL_UP](../hardware/P266_GPIO公共接口.md#gaaa7921da231fd2b96575fa522e2c1970)
- [GPIO_PULL_DOWN](../hardware/P266_GPIO公共接口.md#gadec1802e074f3021d464da09cd66c7cf)

---

[返回大纲](大纲.md) · [下一章](P002_GPIO绑定常量头文件源码.md)
