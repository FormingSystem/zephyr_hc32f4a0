---
id: learning.zephyr-docs.gpio-utils-reference.page-2
title: GPIO辅助头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gpio__utils_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_GPIO辅助头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gpio__utils_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_GPIO辅助头文件参考.md)和[公共API](../hardware/P266_GPIO公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00041"></a>
<a id="foldopen00052"></a>
<a id="foldopen00063"></a>
<a id="foldopen00073"></a>
<a id="foldopen00084"></a>
<a id="foldopen00096"></a>
<a id="foldopen00127"></a>
<a id="adevicetree_8h_html"></a>
<a id="adrivers_2gpio_8h_html"></a>
<a id="aerrno_8h_html"></a>
<a id="agroup__gpio__interface_html_gac7193ccc60e2f1c62569f80cd9973702"></a>
<a id="agroup__gpio__interface_html_gac9d36599625b79bd2ebb9f3603a2a122"></a>
<a id="agroup__single-linked-list__apis_html_ga296560229ffdfd0054c9c7b0602825a6"></a>
<a id="agroup__single-linked-list__apis_html_ga44658c336b634c03938a251cdc8134f8"></a>
<a id="agroup__single-linked-list__apis_html_gac962e3ec8440e4adb2ba6682dbf186ff"></a>
<a id="agroup__single-linked-list__apis_html_gacf3aaf32a6a3389229b548588c6d655e"></a>
<a id="agroup__single-linked-list__apis_html_gaefa93f17fb5412b376360bf06d3e8a78"></a>
<a id="agroup__subsys__tracing__apis__gpio_html_ga9cf081771e5f4724b02de3a89eec339c"></a>
<a id="agroup__subsys__tracing__apis__gpio_html_gaed3026e592853a9a97c0900a0687974b"></a>
<a id="agroup__system__errno_html_ga2d1678d5a7cc8ce499643f3b8957def4"></a>
<a id="aslist_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astructdevice_html"></a>
<a id="astructgpio__callback_html"></a>
<a id="astructgpio__callback_html_ab60e7093072964bd818d536c746211e4"></a>
<a id="astructgpio__callback_html_ace5c2b83f1d51f73877a1f2c54ba8c67"></a>
<a id="astructgpio__callback_html_af89dc41cbd610d81ac03cae7ab764ceb"></a>
<a id="atracing_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2016 Intel Corporation.
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_UTILS_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_UTILS_H_
<a id="l00015"></a>
<a id="l00020"></a>
<a id="l00021"></a>#include &lt;stdbool.h&gt;
<a id="l00022"></a>#include &lt;stdint.h&gt;
<a id="l00023"></a>#include &lt;errno.h&gt;
<a id="l00024"></a>
<a id="l00025"></a>#include &lt;zephyr/devicetree.h&gt;
<a id="l00026"></a>#include &lt;zephyr/drivers/gpio.h&gt;
<a id="l00027"></a>#include &lt;zephyr/sys/__assert.h&gt;
<a id="l00028"></a>#include &lt;zephyr/sys/slist.h&gt;
<a id="l00029"></a>#include &lt;zephyr/tracing/tracing.h&gt;
<a id="l00030"></a>
<a id="l00031"></a>#ifdef __cplusplus
<a id="l00032"></a>extern "C" {
<a id="l00033"></a>#endif
<a id="l00034"></a>
<a id="l00041"></a>#define GPIO_PORT_PIN_MASK_FROM_NGPIOS(ngpios)                  \
<a id="l00042"></a>        ((gpio_port_pins_t)(((uint64_t)1 &lt;&lt; (ngpios)) - 1U))
<a id="l00043"></a>
<a id="l00052"></a>#define GPIO_PORT_PIN_MASK_FROM_DT_NODE(node_id)                \
<a id="l00053"></a>        GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(node_id, DT_PROP(node_id, ngpios))
<a id="l00054"></a>
<a id="l00063"></a>#define GPIO_PORT_PIN_MASK_FROM_DT_INST(inst)                   \
<a id="l00064"></a>        GPIO_PORT_PIN_MASK_FROM_DT_NODE(DT_DRV_INST(inst))
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00073"></a>#define GPIO_COMMON_CONFIG_FROM_DT_NODE(node_id)                           \
<a id="l00074"></a>        {                                                                  \
<a id="l00075"></a>                .port_pin_mask = GPIO_PORT_PIN_MASK_FROM_DT_NODE(node_id), \
<a id="l00076"></a>        }
<a id="l00077"></a>
<a id="l00084"></a>#define GPIO_COMMON_CONFIG_FROM_DT_INST(inst)                   \
<a id="l00085"></a>        GPIO_COMMON_CONFIG_FROM_DT_NODE(DT_DRV_INST(inst))
<a id="l00086"></a>
<a id="l00096"></a>static inline int gpio_manage_callback(sys_slist_t *callbacks,
<a id="l00097"></a>                                        struct gpio_callback *callback,
<a id="l00098"></a>                                        bool set)
<a id="l00099"></a>{
<a id="l00100"></a>        __ASSERT(callback, "No callback!");
<a id="l00101"></a>        __ASSERT(callback-&gt;handler, "No callback handler!");
<a id="l00102"></a>
<a id="l00103"></a>        if (!sys_slist_is_empty(callbacks)) {
<a id="l00104"></a>                if (!sys_slist_find_and_remove(callbacks, &amp;callback-&gt;node)) {
<a id="l00105"></a>                        if (!set) {
<a id="l00106"></a>                                return -EINVAL;
<a id="l00107"></a>                        }
<a id="l00108"></a>                }
<a id="l00109"></a>        } else if (!set) {
<a id="l00110"></a>                return -EINVAL;
<a id="l00111"></a>        }
<a id="l00112"></a>
<a id="l00113"></a>        if (set) {
<a id="l00114"></a>                sys_slist_prepend(callbacks, &amp;callback-&gt;node);
<a id="l00115"></a>        }
<a id="l00116"></a>
<a id="l00117"></a>        return 0;
<a id="l00118"></a>}
<a id="l00119"></a>
<a id="l00127"></a>static inline void gpio_fire_callbacks(sys_slist_t *list,
<a id="l00128"></a>                                        const struct device *port,
<a id="l00129"></a>                                        uint32_t pins)
<a id="l00130"></a>{
<a id="l00131"></a>        struct gpio_callback *cb, *tmp;
<a id="l00132"></a>
<a id="l00133"></a>        sys_port_trace_gpio_fire_callbacks_enter(list, port, pins);
<a id="l00134"></a>
<a id="l00135"></a>        SYS_SLIST_FOR_EACH_CONTAINER_SAFE(list, cb, tmp, node) {
<a id="l00136"></a>                if (cb-&gt;pin_mask &amp; pins) {
<a id="l00137"></a>                        __ASSERT(cb-&gt;handler, "No callback handler!");
<a id="l00138"></a>
<a id="l00139"></a>                        cb-&gt;handler(port, cb, cb-&gt;pin_mask &amp; pins);
<a id="l00140"></a>                        sys_port_trace_gpio_fire_callback(port, cb);
<a id="l00141"></a>                }
<a id="l00142"></a>        }
<a id="l00143"></a>}
<a id="l00144"></a>
<a id="l00145"></a>#ifdef __cplusplus
<a id="l00146"></a>}
<a id="l00147"></a>#endif
<a id="l00148"></a>
<a id="l00152"></a>
<a id="l00153"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_UTILS_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2016 Intel Corporation.；Apache-2.0许可证原文保留。

2. 结束GPIO辅助头文件包含保护（Include Guard）ZEPHYR_INCLUDE_DRIVERS_GPIO_GPIO_UTILS_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

### `devicetree.h`

设备树（Devicetree）主头文件。

符号定位：[devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)。

### `gpio.h`

GPIO（通用输入输出）驱动API的主头文件。

符号定位：[gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)。

### `errno.h`

系统错误编号（System Error Numbers）。

符号定位：[errno.h](../error_reference/P004_错误号头文件参考.md)。

### `gpio_fire_callbacks`

```c
static void gpio_fire_callbacks(sys_slist_t *list, const struct device *port, uint32_t pins)
```

遍历回调链表并触发回调的通用函数。

定义位置（Definition）：gpio_utils.h:127。

符号定位：[gpio_fire_callbacks](../hardware/P266_GPIO公共接口.md#gac7193ccc60e2f1c62569f80cd9973702)。

### `gpio_manage_callback`

```c
static int gpio_manage_callback(sys_slist_t *callbacks, struct gpio_callback *callback, bool set)
```

在回调链表（Callback List）中插入或移除回调的通用函数。

定义位置（Definition）：gpio_utils.h:96。

符号定位：[gpio_manage_callback](../hardware/P266_GPIO公共接口.md#gac9d36599625b79bd2ebb9f3603a2a122)。

### `sys_slist_find_and_remove`

```c
static bool sys_slist_find_and_remove(sys_slist_t *list, sys_snode_t *node)
```

从链表中查找并移除一个节点（Node）。

定义位置（Definition）：slist.h:453。

符号定位：[sys_slist_find_and_remove](../slist_reference/P001_单向链表公共接口.md#ga296560229ffdfd0054c9c7b0602825a6)。

### `sys_slist_t`

```c
struct _slist sys_slist_t
```

单向链表（Singly Linked List）结构。

定义位置（Definition）：slist.h:54。

符号定位：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)。

### `sys_slist_prepend`

```c
static void sys_slist_prepend(sys_slist_t *list, sys_snode_t *node)
```

将节点插入给定链表的头部（Prepend）。

定义位置（Definition）：slist.h:310。

符号定位：[sys_slist_prepend](../slist_reference/P001_单向链表公共接口.md#gac962e3ec8440e4adb2ba6682dbf186ff)。

### `SYS_SLIST_FOR_EACH_CONTAINER_SAFE`

```c
#define SYS_SLIST_FOR_EACH_CONTAINER_SAFE(__sl, __cn, __cns, __n)
```

提供按容器（Container）安全遍历链表的基本操作。注意：__cn可以脱离链表……（原符号提示在此截断）。

定义位置（Definition）：slist.h:188。

符号定位：[SYS_SLIST_FOR_EACH_CONTAINER_SAFE](../slist_reference/P001_单向链表公共接口.md#gacf3aaf32a6a3389229b548588c6d655e)。

### `sys_slist_is_empty`

```c
static bool sys_slist_is_empty(const sys_slist_t *list)
```

检查给定链表是否为空。

定义位置（Definition）：slist.h:273。

符号定位：[sys_slist_is_empty](../slist_reference/P001_单向链表公共接口.md#gaefa93f17fb5412b376360bf06d3e8a78)。

### `sys_port_trace_gpio_fire_callbacks_enter`

```c
#define sys_port_trace_gpio_fire_callbacks_enter(list, port, pins)
```

定义位置（Definition）：tracing_hooks.h:3341。

符号定位：[sys_port_trace_gpio_fire_callbacks_enter](../driver_trace_reference/P002_GPIO跟踪接口.md#ga9cf081771e5f4724b02de3a89eec339c)。

### `sys_port_trace_gpio_fire_callback`

```c
#define sys_port_trace_gpio_fire_callback(port, callback)
```

定义位置（Definition）：tracing_hooks.h:3350。

符号定位：[sys_port_trace_gpio_fire_callback](../driver_trace_reference/P002_GPIO跟踪接口.md#gaed3026e592853a9a97c0900a0687974b)。

### `EINVAL`

```c
#define EINVAL
```

参数无效（Invalid Argument）。

定义位置（Definition）：errno.h:61。

符号定位：[EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)。

### `slist.h`

单向链表API头文件。

符号定位：[slist.h](../slist_reference/P002_单向链表头文件参考.md)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `device`

每个驱动实例的运行时设备结构，位于只读存储器（ROM）中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `gpio_callback`

GPIO回调结构（Callback Structure）。

定义位置（Definition）：gpio.h:771。

符号定位：[gpio_callback](../hardware/P270_GPIO回调结构.md)。

### `gpio_callback::node`

```c
sys_snode_t node
```

供驱动内部使用，用户不应修改它；参见drivers/gpio/gpio_ut……（原符号提示在此截断）。

定义位置（Definition）：gpio.h:775。

符号定位：[gpio_callback::node](../hardware/P270_GPIO回调结构.md#ab60e7093072964bd818d536c746211e4)。

### `gpio_callback::pin_mask`

```c
gpio_port_pins_t pin_mask
```

回调关注的引脚掩码；为0时永远不会调用此回调。

定义位置（Definition）：gpio.h:786。

符号定位：[gpio_callback::pin_mask](../hardware/P270_GPIO回调结构.md#ace5c2b83f1d51f73877a1f2c54ba8c67)。

### `gpio_callback::handler`

```c
gpio_callback_handler_t handler
```

条件符合时实际调用的回调函数。

定义位置（Definition）：gpio.h:778。

符号定位：[gpio_callback::handler](../hardware/P270_GPIO回调结构.md#af89dc41cbd610d81ac03cae7ab764ceb)。

### `tracing.h`

跟踪子系统（Tracing Subsystem）API的主头文件。

符号定位：[tracing.h](../tracing_core_reference/P007_跟踪公共头文件参考.md)。

## 2.4\_源码跟踪译注

> 译注——辅助层与公共接口：本头文件供GPIO驱动复用，gpio_manage_callback接收驱动持有的链表，gpio_fire_callbacks由驱动在事件处理路径调用。应用通常使用gpio_init_callback、gpio_add_callback以及gpio_pin_interrupt_configure；管理链表本身不会配置引脚，也不会使能硬件中断。完整接口说明见既有GPIO公共接口页。

> 译注——数量与掩码：GPIO_PORT_PIN_MASK_FROM_NGPIOS使用64位移位生成低ngpios位，再转换为32位gpio_port_pins_t。ngpios=0得到0，32得到全部32个有效位；64位中间值用于容纳32位端口的边界，并不把GPIO端口扩展到64位。宏没有为任意负数或过大数量提供运行期验证，调用方应遵守端口位宽范围。

> 译注——设备树与保留区：FROM_DT_NODE通过GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC读取ngpios并排除gpio-reserved-ranges；FROM_DT_INST先把DT_DRV_COMPAT实例编号转换为节点标识符。COMMON_CONFIG宏生成带.port_pin_mask的结构初始化器，不读取硬件，也不动态分配或注册设备。公共配置应放在驱动私有配置的首成员，才能由通用GPIO包装按共同前缀访问。

> 译注——重复注册与删除：gpio_manage_callback先查找并移除同一个callback->node，再在set=true时插入链表头部。再次添加已有回调会改变其顺序，不能理解为追加第二份副本。set=false删除不存在节点或从空链表删除时返回-EINVAL；成功返回0。回调节点属于调用者提供的结构，函数没有分配或释放它，也不能让同一节点同时属于多个链表。

> 译注——空链表不等于空指针：原公共接口参数说明将callbacks标为可为NULL，但当前辅助实现直接调用sys_slist_is_empty，而后者读取链表头；这里应传入有效且已初始化的链表对象，空链表用对象的空head表示。对callback及handler使用的是断言，断言关闭后不能期待自动返回参数错误。本译注说明实现边界，未修改原接口说明。

> 译注——触发的引脚集合：gpio_fire_callbacks按链表顺序检查cb->pin_mask与pins的交集，非空时同步调用handler(port, cb, intersection)。回调收到的是自己关注且本次触发的引脚，不是整个端口的所有输入值；掩码为0不会调用处理函数。这一函数不清除硬件中断状态，也不自动把处理工作搬到工作队列。

> 译注——安全遍历与生存期：SYS_SLIST_FOR_EACH_CONTAINER_SAFE在调用处理函数前保存下一个容器指针，允许当前节点脱离链表，不等于允许任意并发删除或销毁下一个节点。单向链表API明确不是线程安全的，辅助函数没有增加锁。回调返回后还有跟踪调用使用当前cb指针，因此移除注册和释放对象是两个不同动作，不能据遍历宏名称推导出可以立即销毁回调对象。具体执行上下文与同步方式还须核对调用此辅助函数的驱动。

> 译注——版本边界：本批核对GPIO辅助头文件、GPIO公共头文件、单向链表头文件和通用链表宏四份官方源码并记录摘要；源码页的非注释代码与读取的官方辅助头文件一致。latest、滚动main及仓库版本不自动相同，源码定位使用仓库相对链接。本次未构建固件、触发实板GPIO中断或操作硬件。

头文件相对定位：[include/zephyr/drivers/gpio/gpio_utils.h](../../../include/zephyr/drivers/gpio/gpio_utils.h)，关联实现／接口：[include/zephyr/sys/slist.h](../../../include/zephyr/sys/slist.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/gpio/gpio_utils.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/slist.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、触发实板GPIO中断或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_GPIO辅助头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [errno.h](../error_reference/P004_错误号头文件参考.md)
- [zephyr/devicetree.h](../dt_main_reference/P001_设备树主头文件参考.md)
- [zephyr/drivers/gpio.h](../gpio_driver_reference/P001_GPIO驱动头文件参考.md)
- [zephyr/sys/slist.h](../slist_reference/P002_单向链表头文件参考.md)
- [zephyr/tracing/tracing.h](../tracing_core_reference/P007_跟踪公共头文件参考.md)
- [gpio_manage_callback](../hardware/P266_GPIO公共接口.md#gac9d36599625b79bd2ebb9f3603a2a122)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [gpio_callback](../hardware/P270_GPIO回调结构.md)
- [handler](../hardware/P270_GPIO回调结构.md#af89dc41cbd610d81ac03cae7ab764ceb)
- [sys_slist_is_empty](../slist_reference/P001_单向链表公共接口.md#gaefa93f17fb5412b376360bf06d3e8a78)
- [sys_slist_find_and_remove](../slist_reference/P001_单向链表公共接口.md#ga296560229ffdfd0054c9c7b0602825a6)
- [node](../hardware/P270_GPIO回调结构.md#ab60e7093072964bd818d536c746211e4)
- [EINVAL](../error_reference/P003_系统错误号公共接口.md#ga2d1678d5a7cc8ce499643f3b8957def4)
- [sys_slist_prepend](../slist_reference/P001_单向链表公共接口.md#gac962e3ec8440e4adb2ba6682dbf186ff)
- [gpio_fire_callbacks](../hardware/P266_GPIO公共接口.md#gac7193ccc60e2f1c62569f80cd9973702)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [sys_port_trace_gpio_fire_callbacks_enter](../driver_trace_reference/P002_GPIO跟踪接口.md#ga9cf081771e5f4724b02de3a89eec339c)
- [SYS_SLIST_FOR_EACH_CONTAINER_SAFE](../slist_reference/P001_单向链表公共接口.md#gacf3aaf32a6a3389229b548588c6d655e)
- [pin_mask](../hardware/P270_GPIO回调结构.md#ace5c2b83f1d51f73877a1f2c54ba8c67)
- [sys_port_trace_gpio_fire_callback](../driver_trace_reference/P002_GPIO跟踪接口.md#gaed3026e592853a9a97c0900a0687974b)

---

[上一章](P001_GPIO辅助头文件参考.md) · [返回大纲](大纲.md)
