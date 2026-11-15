---
id: learning.zephyr-docs.gpio-utils-reference.page-1
title: GPIO辅助头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__utils_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_GPIO辅助头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gpio__utils_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入GPIO辅助头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

GPIO（通用输入输出，General-purpose Input/Output）辅助函数（Utility Functions）的头文件。

<a id="details"></a>

```c
#include <stdbool.h>
#include <stdint.h>
#include <errno.h>
#include <zephyr/devicetree.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/sys/__assert.h>
#include <zephyr/sys/slist.h>
#include <zephyr/tracing/tracing.h>
```

查看此文件的源码。

GPIO（通用输入输出，General-purpose Input/Output）辅助函数（Utility Functions）的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_ga696fbe0e6868902fbec77afc06f55e0a"></a>

```c
#define GPIO_PORT_PIN_MASK_FROM_NGPIOS(ngpios)
```

相关声明：[GPIO_PORT_PIN_MASK_FROM_NGPIOS](../hardware/P266_GPIO公共接口.md#ga696fbe0e6868902fbec77afc06f55e0a)。

根据GPIO数量生成允许使用的GPIO位掩码（Bitmask）。

<a id="r_ga570c8e724c799b1bb0edeafa249d9730"></a>

```c
#define GPIO_PORT_PIN_MASK_FROM_DT_NODE(node_id)
```

相关声明：[GPIO_PORT_PIN_MASK_FROM_DT_NODE](../hardware/P266_GPIO公共接口.md#ga570c8e724c799b1bb0edeafa249d9730)。

根据设备树（Devicetree）的gpio-reserved-ranges与ngpios属性值生成允许使用的GPIO位掩码。

<a id="r_ga34528b682ca57bfc77cef745ed235e04"></a>

```c
#define GPIO_PORT_PIN_MASK_FROM_DT_INST(inst)
```

相关声明：[GPIO_PORT_PIN_MASK_FROM_DT_INST](../hardware/P266_GPIO公共接口.md#ga34528b682ca57bfc77cef745ed235e04)。

根据DT_DRV_COMPAT实例的GPIO gpio-reserved-ranges与ngpios设备树属性值生成允许使用的GPIO位掩码。

<a id="r_ga7b248bc1a6d7b922df7dae15b7c7855f"></a>

```c
#define GPIO_COMMON_CONFIG_FROM_DT_NODE(node_id)
```

相关声明：[GPIO_COMMON_CONFIG_FROM_DT_NODE](../hardware/P266_GPIO公共接口.md#ga7b248bc1a6d7b922df7dae15b7c7855f)。

根据节点标识符（Node Identifier）生成struct gpio_driver_config初始化器。

<a id="r_gafa496e01d480334049c9bb574267659d"></a>

```c
#define GPIO_COMMON_CONFIG_FROM_DT_INST(inst)
```

相关声明：[GPIO_COMMON_CONFIG_FROM_DT_INST](../hardware/P266_GPIO公共接口.md#gafa496e01d480334049c9bb574267659d)。

根据DT_DRV_COMPAT实例编号生成struct gpio_driver_config初始化器。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.2\_函数（Functions）

<a id="r_gac9d36599625b79bd2ebb9f3603a2a122"></a>

```c
static int gpio_manage_callback (sys_slist_t *callbacks, struct gpio_callback *callback, bool set)
```

相关声明：[gpio_manage_callback](../hardware/P266_GPIO公共接口.md#gac9d36599625b79bd2ebb9f3603a2a122)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[gpio_callback](../hardware/P270_GPIO回调结构.md)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

在回调链表（Callback List）中插入或移除回调的通用函数。

<a id="r_gac7193ccc60e2f1c62569f80cd9973702"></a>

```c
static void gpio_fire_callbacks (sys_slist_t *list, const struct device *port, uint32_t pins)
```

相关声明：[gpio_fire_callbacks](../hardware/P266_GPIO公共接口.md#gac7193ccc60e2f1c62569f80cd9973702)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

遍历回调链表并触发回调的通用函数。

## 1.3\_源码定位与版本边界

相对源码定位：[GPIO辅助头文件](../../../include/zephyr/drivers/gpio/gpio_utils.h)、[GPIO公共头文件](../../../include/zephyr/drivers/gpio.h)、[单向链表](../../../include/zephyr/sys/slist.h)和[通用链表宏](../../../include/zephyr/sys/list_gen.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：辅助层与公共接口：本头文件供GPIO驱动复用，gpio_manage_callback接收驱动持有的链表，gpio_fire_callbacks由驱动在事件处理路径调用。应用通常使用gpio_init_callback、gpio_add_callback以及gpio_pin_interrupt_configure；管理链表本身不会配置引脚，也不会使能硬件中断。完整接口说明见既有GPIO公共接口页。

> 译注——源码核对：数量与掩码：GPIO_PORT_PIN_MASK_FROM_NGPIOS使用64位移位生成低ngpios位，再转换为32位gpio_port_pins_t。ngpios=0得到0，32得到全部32个有效位；64位中间值用于容纳32位端口的边界，并不把GPIO端口扩展到64位。宏没有为任意负数或过大数量提供运行期验证，调用方应遵守端口位宽范围。

> 译注——源码核对：设备树与保留区：FROM_DT_NODE通过GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC读取ngpios并排除gpio-reserved-ranges；FROM_DT_INST先把DT_DRV_COMPAT实例编号转换为节点标识符。COMMON_CONFIG宏生成带.port_pin_mask的结构初始化器，不读取硬件，也不动态分配或注册设备。公共配置应放在驱动私有配置的首成员，才能由通用GPIO包装按共同前缀访问。

> 译注——源码核对：重复注册与删除：gpio_manage_callback先查找并移除同一个callback->node，再在set=true时插入链表头部。再次添加已有回调会改变其顺序，不能理解为追加第二份副本。set=false删除不存在节点或从空链表删除时返回-EINVAL；成功返回0。回调节点属于调用者提供的结构，函数没有分配或释放它，也不能让同一节点同时属于多个链表。

> 译注——源码核对：空链表不等于空指针：原公共接口参数说明将callbacks标为可为NULL，但当前辅助实现直接调用sys_slist_is_empty，而后者读取链表头；这里应传入有效且已初始化的链表对象，空链表用对象的空head表示。对callback及handler使用的是断言，断言关闭后不能期待自动返回参数错误。本译注说明实现边界，未修改原接口说明。

> 译注——源码核对：触发的引脚集合：gpio_fire_callbacks按链表顺序检查cb->pin_mask与pins的交集，非空时同步调用handler(port, cb, intersection)。回调收到的是自己关注且本次触发的引脚，不是整个端口的所有输入值；掩码为0不会调用处理函数。这一函数不清除硬件中断状态，也不自动把处理工作搬到工作队列。

> 译注——源码核对：安全遍历与生存期：SYS_SLIST_FOR_EACH_CONTAINER_SAFE在调用处理函数前保存下一个容器指针，允许当前节点脱离链表，不等于允许任意并发删除或销毁下一个节点。单向链表API明确不是线程安全的，辅助函数没有增加锁。回调返回后还有跟踪调用使用当前cb指针，因此移除注册和释放对象是两个不同动作，不能据遍历宏名称推导出可以立即销毁回调对象。具体执行上下文与同步方式还须核对调用此辅助函数的驱动。

> 译注——源码核对：版本边界：本批核对GPIO辅助头文件、GPIO公共头文件、单向链表头文件和通用链表宏四份官方源码并记录摘要；源码页的非注释代码与读取的官方辅助头文件一致。latest、滚动main及仓库版本不自动相同，源码定位使用仓库相对链接。本次未构建固件、触发实板GPIO中断或操作硬件。

本次验证范围为文档与源码对照，未构建固件、触发实板GPIO中断或操作硬件。

## 1.4\_原页交叉引用（Cross References）

- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/tracing/tracing.h](../tracing_headers_reference/P001_跟踪公共头文件源码.md)
- [查看此文件的源码](P002_GPIO辅助头文件源码.md)
- [GPIO_PORT_PIN_MASK_FROM_NGPIOS](../hardware/P266_GPIO公共接口.md#ga696fbe0e6868902fbec77afc06f55e0a)
- [GPIO_PORT_PIN_MASK_FROM_DT_NODE](../hardware/P266_GPIO公共接口.md#ga570c8e724c799b1bb0edeafa249d9730)
- [GPIO_PORT_PIN_MASK_FROM_DT_INST](../hardware/P266_GPIO公共接口.md#ga34528b682ca57bfc77cef745ed235e04)
- [GPIO_COMMON_CONFIG_FROM_DT_NODE](../hardware/P266_GPIO公共接口.md#ga7b248bc1a6d7b922df7dae15b7c7855f)
- [gpio_driver_config](../hardware/P268_GPIO公共驱动配置.md)
- [GPIO_COMMON_CONFIG_FROM_DT_INST](../hardware/P266_GPIO公共接口.md#gafa496e01d480334049c9bb574267659d)
- [gpio_manage_callback](../hardware/P266_GPIO公共接口.md#gac9d36599625b79bd2ebb9f3603a2a122)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [gpio_fire_callbacks](../hardware/P266_GPIO公共接口.md#gac7193ccc60e2f1c62569f80cd9973702)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_GPIO辅助头文件源码.md)
