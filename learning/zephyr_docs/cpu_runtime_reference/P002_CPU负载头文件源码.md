---
id: learning.zephyr-docs.cpu-runtime-reference.page-2
title: CPU负载头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cpu__load_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_CPU负载头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cpu__load_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_CPU负载头文件参考.md)和[公共API](../observability/P049_CPU负载接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00110"></a>
<a id="agroup__cpu__load_html_ga21c1e9efe2f4ba8f40a3e9dd1f32b52e"></a>
<a id="agroup__cpu__load_html_ga28a73232eb45cdf6ce057e1e4c84190d"></a>
<a id="agroup__cpu__load_html_ga3333539cf7d8a6916cbbec9cd1f5bf59"></a>
<a id="agroup__cpu__load_html_ga83f2e3099de11b8e6b66395ae69f394a"></a>
<a id="agroup__cpu__load_html_ga8a8c97914a72b6eb5a7e1862710a0c6d"></a>
<a id="agroup__cpu__load_html_gab8e384170b8fc3c253a30e3490ebb34f"></a>
<a id="agroup__cpu__load_html_gabc95920fb1a666b1496618cf5afbfbff"></a>
<a id="agroup__cpu__load_html_gaec80c70d8dd6ea130edde48618ed2463"></a>
<a id="agroup__cpu__load_html_gaf44501a292aeef7749b68c706b34119f"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="atoolchain_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024, Nordic Semiconductor ASA
<a id="l00003"></a> * Copyright (c) 2025 Analog Devices, Inc.
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00008"></a>#ifndef ZEPHYR_INCLUDE_SYS_CPU_LOAD_H_
<a id="l00009"></a>#define ZEPHYR_INCLUDE_SYS_CPU_LOAD_H_
<a id="l00010"></a>
<a id="l00011"></a>#include &lt;stdbool.h&gt;
<a id="l00012"></a>#include &lt;stdint.h&gt;
<a id="l00013"></a>#include &lt;zephyr/toolchain.h&gt;
<a id="l00014"></a>
<a id="l00015"></a>#ifdef __cplusplus
<a id="l00016"></a>extern "C" {
<a id="l00017"></a>#endif
<a id="l00018"></a>
<a id="l00038"></a>
<a id="l00040"></a>#define CPU_LOAD_PERMILLE_TO_PERCENT(permille) ((permille) / 10)
<a id="l00041"></a>
<a id="l00050"></a>int cpu_load_get_cpu(unsigned int cpu_id, bool reset);
<a id="l00051"></a>
<a id="l00059"></a>int cpu_load_get(bool reset);
<a id="l00060"></a>
<a id="l00065"></a>void cpu_load_on_enter_idle(void);
<a id="l00066"></a>
<a id="l00071"></a>void cpu_load_on_exit_idle(void);
<a id="l00072"></a>
<a id="l00079"></a>void cpu_load_log_control(bool enable);
<a id="l00080"></a>
<a id="l00081"></a>/* Optional callback for cpu_load_cb_reg
<a id="l00082"></a> *
<a id="l00083"></a> * This will be called from the k_timer expiry_fn used for periodic logging.
<a id="l00084"></a> * CONFIG_CPU_LOAD_LOG_PERIODICALLY must be configured to a positive value.
<a id="l00085"></a> * Time spent in this callback must be kept to a minimum.
<a id="l00086"></a> */
<a id="l00087"></a>typedef void (*cpu_load_cb_t)(uint8_t percent);
<a id="l00088"></a>
<a id="l00098"></a>int cpu_load_cb_reg(cpu_load_cb_t cb, uint8_t threshold_percent);
<a id="l00099"></a>
<a id="l00110"></a>__deprecated static inline int cpu_load_metric_get(int cpu_id)
<a id="l00111"></a>{
<a id="l00112"></a>        int load = cpu_load_get_cpu((unsigned int)cpu_id, true);
<a id="l00113"></a>
<a id="l00114"></a>        return (load &lt; 0) ? load : CPU_LOAD_PERMILLE_TO_PERCENT(load);
<a id="l00115"></a>}
<a id="l00116"></a>
<a id="l00120"></a>
<a id="l00121"></a>#ifdef __cplusplus
<a id="l00122"></a>}
<a id="l00123"></a>#endif
<a id="l00124"></a>
<a id="l00125"></a>#endif /* ZEPHYR_INCLUDE_SYS_CPU_LOAD_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024, Nordic Semiconductor ASA；Copyright (c) 2025 Analog Devices, Inc.；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. cpu_load_cb_reg的可选回调（Optional Callback）。它由周期日志使用的k_timer到期函数expiry_fn调用。CONFIG_CPU_LOAD_LOG_PERIODICALLY必须配置为正值。应尽量缩短此回调的执行时间。

3. ZEPHYR_INCLUDE_SYS_CPU_LOAD_H_头文件包含保护结束。

## 2.3\_原页符号提示（Symbol Descriptions）

### `CPU_LOAD_PERMILLE_TO_PERCENT`

```c
#define CPU_LOAD_PERMILLE_TO_PERCENT(permille)
```

将千分比（Per Mille）形式的 CPU 负载转换为整数百分比（Whole Percent）。

定义位置（Definition）：cpu_load.h:40。

符号定位：[CPU_LOAD_PERMILLE_TO_PERCENT](../observability/P049_CPU负载接口.md#ga21c1e9efe2f4ba8f40a3e9dd1f32b52e)。

### `cpu_load_on_enter_idle`

```c
void cpu_load_on_enter_idle(void)
```

进入 CPU 空闲状态（Idle）时调用的钩子（Hook）。

符号定位：[cpu_load_on_enter_idle](../observability/P049_CPU负载接口.md#ga28a73232eb45cdf6ce057e1e4c84190d)。

### `cpu_load_metric_get`

```c
static int cpu_load_metric_get(int cpu_id)
```

获取指定 CPU 的负载百分比。

定义位置（Definition）：cpu_load.h:110。

符号定位：[cpu_load_metric_get](../observability/P049_CPU负载接口.md#ga3333539cf7d8a6916cbbec9cd1f5bf59)。

### `cpu_load_cb_t`

```c
void(* cpu_load_cb_t)(uint8_t percent)
```

定义位置（Definition）：cpu_load.h:87。

符号定位：[cpu_load_cb_t](../observability/P049_CPU负载接口.md#ga83f2e3099de11b8e6b66395ae69f394a)。

### `cpu_load_on_exit_idle`

```c
void cpu_load_on_exit_idle(void)
```

退出 CPU 空闲状态时调用的钩子。

符号定位：[cpu_load_on_exit_idle](../observability/P049_CPU负载接口.md#ga8a8c97914a72b6eb5a7e1862710a0c6d)。

### `cpu_load_get_cpu`

```c
int cpu_load_get_cpu(unsigned int cpu_id, bool reset)
```

获取指定 CPU 的负载（CPU Load）。

符号定位：[cpu_load_get_cpu](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)。

### `cpu_load_log_control`

```c
void cpu_load_log_control(bool enable)
```

控制周期性 CPU 负载报告。

符号定位：[cpu_load_log_control](../observability/P049_CPU负载接口.md#gabc95920fb1a666b1496618cf5afbfbff)。

### `cpu_load_cb_reg`

```c
int cpu_load_cb_reg(cpu_load_cb_t cb, uint8_t threshold_percent)
```

可选的回调注册：当负载大于或等于阈值（Threshold）时调用回调。

符号定位：[cpu_load_cb_reg](../observability/P049_CPU负载接口.md#gaec80c70d8dd6ea130edde48618ed2463)。

### `cpu_load_get`

```c
int cpu_load_get(bool reset)
```

获取当前 CPU 的负载。

符号定位：[cpu_load_get](../observability/P049_CPU负载接口.md#gaf44501a292aeef7749b68c706b34119f)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `toolchain.h`

用于抽象工具链（Toolchain）特有能力的宏。

符号定位：[toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)。

## 2.4\_源码跟踪译注

> 译注——cpu_load_get_cpu和cpu_load_get返回千分比（Per Mille）0～1000，失败返回负errno；先检查负值再转换单位。CPU_LOAD_PERMILLE_TO_PERCENT只是除以10，整数输入会舍去小数，不负责错误检查。旧cpu_load_metric_get返回整数百分比，并固定传入reset=true，迁移接口时单位和采样窗口都要明确。

> 译注——reset=true在取得当前读数后更新目标CPU的测量窗口（Measurement Window）。运行统计后端更新自身保存的active_prev和wall_prev，并不清零调度器的累计计数；多个调用者读取同一CPU并重置时会共享这个窗口。周期报告也逐CPU调用reset=true，会影响手动读取的区间。

> 译注——周期回调从k_timer到期函数（Expiry Function）执行，CONFIG_CPU_LOAD_LOG_PERIODICALLY须为正值；注册回调本身不会启动独立采样线程。当前实现先把千分比除以10，再与0～100的阈值比较，每个达到阈值的CPU都可能触发回调；回调参数只有百分比，没有CPU编号。

> 译注——运行统计后端（Runtime Statistics Backend）按非空闲周期差值除以总周期差值计算负载；空闲钩子后端（Idle Hook Backend）按经过时间减去空闲时间计算。可选硬件计数器路径受!SMP限制，不能把这一限制推广到整个空闲钩子实现；本次源码已有按CPU保存的空闲窗口。Kconfig仍有单CPU概括文字，应结合实际条件与实现核对。

> 译注——cpu_load_log_control(true)在正的报告周期下先重置所有CPU测量窗口，再启动定时器；false停止报告，不等于停止后端统计。周期配置为0时此函数直接返回。

头文件相对定位：[include/zephyr/sys/cpu_load.h](../../../include/zephyr/sys/cpu_load.h)，关联实现／接口：[lib/os/cpu_load/cpu_load.c](../../../lib/os/cpu_load/cpu_load.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/sys/cpu_load.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/os/cpu_load/cpu_load.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_CPU负载头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/toolchain.h](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)
- [cpu_load_get_cpu](../observability/P049_CPU负载接口.md#gab8e384170b8fc3c253a30e3490ebb34f)
- [cpu_load_get](../observability/P049_CPU负载接口.md#gaf44501a292aeef7749b68c706b34119f)
- [cpu_load_on_enter_idle](../observability/P049_CPU负载接口.md#ga28a73232eb45cdf6ce057e1e4c84190d)
- [cpu_load_on_exit_idle](../observability/P049_CPU负载接口.md#ga8a8c97914a72b6eb5a7e1862710a0c6d)
- [cpu_load_log_control](../observability/P049_CPU负载接口.md#gabc95920fb1a666b1496618cf5afbfbff)
- [cpu_load_cb_t](../observability/P049_CPU负载接口.md#ga83f2e3099de11b8e6b66395ae69f394a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cpu_load_cb_reg](../observability/P049_CPU负载接口.md#gaec80c70d8dd6ea130edde48618ed2463)
- [cpu_load_metric_get](../observability/P049_CPU负载接口.md#ga3333539cf7d8a6916cbbec9cd1f5bf59)
- [CPU_LOAD_PERMILLE_TO_PERCENT](../observability/P049_CPU负载接口.md#ga21c1e9efe2f4ba8f40a3e9dd1f32b52e)

---

[上一章](P001_CPU负载头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_CPU负载指标头文件参考.md)
