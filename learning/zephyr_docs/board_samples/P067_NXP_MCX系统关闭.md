---
id: learning.zephyr-docs.board-samples.page-67
title: NXP_MCX系统关闭
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/mcxn_a/system_off/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nxp_mcx_system_off"></a>

# 第67章\_NXP MCX 系统关闭（NXP MCX system off）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/mcxn_a/system_off/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/mcxn_a/system_off/README.rst/..)

<a id="overview"></a>

## 67.1 概述（Overview）

本示例使 NXP MCXA 或 MCXN SoC 进入系统关闭，对应 SoC 的深度掉电（Deep Power Down）模式。该模式关闭 CORE 电源域，芯片通过复位流程唤醒，因此唤醒表现类似冷启动（Cold boot）。

示例执行 `CONFIG_SAMPLE_APP_TEST_CYCLES` 次系统关闭循环，默认十次，随后停止并打印最终的 `Completed N system-off cycles`，供测试框架确认每次唤醒均发生。不需要控制台输入。

每次唤醒都会复位，因此已完成循环的计数必须跨深度掉电保留。深度掉电关闭所有 SRAM 阵列，所以示例把计数存放在保持 SRAM 中，并在关闭前启用其低功耗保持：MCXN 使用 VBAT SRAM LDO，MCXA 使用 SPC SRAM 保持 LDO。每次启动时，通过 hwinfo 报告的复位原因 `RESET_LOW_POWER_WAKE` 区分唤醒和冷启动；冷启动初始化计数，唤醒则继续计数。达到目标次数后，示例直接返回，不再关闭，SoC 保持唤醒且可调试。 相关链接：[硬件信息（hwinfo）](../hardware/P020_硬件信息.md#hwinfo-api)。

> 译注——保持实现的版本细节：本次代码把 MCXN 与 MCXAxx7 放在 VBAT 分支，其余 MCXA 使用 SPC 分支，不能仅按 MCXA 系列名称统一选择。LDO 是低压差稳压器（Low-Dropout Regulator）；保持供电与 noinit 段安排缺一不可。MCXN overlay 将 SRAM 映射到 RAMA1～RAMA3，避开 ROM 临时区。

唤醒源通过[唤醒控制器（Wakeup Controller，WUC）](../hardware/P103_唤醒控制器.md#wuc-api)子系统配置，使用 `nxp,wuc-wuu` 驱动。构建时可选择以下两种唤醒源：

- `CONFIG_SAMPLE_SYSTEM_OFF_WAKEUP_TIMER` 为默认选项，通过计数器闹钟 API 启用 LPTMR0，并将其作为 WUU 内部模块唤醒源路由到内核，因此开发板几秒后自动唤醒，无需外部操作。

- `CONFIG_SAMPLE_SYSTEM_OFF_WAKEUP_BUTTON` 等待 WUU 外部引脚发生电平转换。开发板设备树将 WUU 源附到唤醒按钮节点上，与按钮的 `gpios` 并列，并设置 `wakeup-button` 别名；示例只需启用 `DT_ALIAS(wakeup_button)`，不需要示例覆盖文件。开发板可这样描述：

```text
&user_button_2 {
    wakeup-ctrls = <&wuu NXP_WUU_PIN_0_FALLING_INT>;
};

/ {
    aliases {
        wakeup-button = &user_button_2;
    };
};
```

<a id="building-and-running"></a>

## 67.2 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具链、模块及对应板。构建产物由工具生成，下载与启动按具体板文档核对。本次未执行构建、烧录或硬件测量。

使用默认的定时器唤醒源构建并烧录示例：

> 译注——覆盖文件边界：原文“不需要示例覆盖文件”针对按钮的 WUU 唤醒节点描述；并不代表保持内存和低功耗状态不需要配置。本次 tests.yaml 的 MCXN 定时器测试明确同时使用 mcx.overlay、mcxn.overlay；普通 west build 不会自动套用 Twister 测试条目的 extra_dtc_overlay_files。复制原命令前，应核对所选版本如何提供这些设置，不能把默认命令和测试配置视为完全相同。

```text
west build -b frdm_mcxn947/mcxn947/cpu0 samples/boards/nxp/mcxn_a/system_off
west flash
```

<a id="sample-output"></a>

## 67.3 输出示例（Sample Output）

```text
frdm_mcxn236 system off demo
Entering system off (cycle 1/10); the timer wakes it in 5 s
<the timer wakes the SoC after 5 s through the reset routine; main() restarts>
frdm_mcxn236 system off demo
Woke from system off; retained count 1/10
Entering system off (cycle 2/10); the timer wakes it in 5 s
...
frdm_mcxn236 system off demo
Woke from system off; retained count 10/10
Completed 10 system-off cycles
```

选择 `CONFIG_SAMPLE_SYSTEM_OFF_WAKEUP_BUTTON` 后，每个循环改为等待按下开发板的唤醒按钮 SW2，以退出系统关闭状态。

> 译注——唤醒与日志：默认 LPTMR0 闹钟为五秒，按钮唤醒则等待实际外部输入。WUU 是唤醒单元（Wakeup Unit）；SW2 和对应引脚由板定义。上面的构建目标是 frdm_mcxn947，原始输出来自 frdm_mcxn236，板名不同不代表构建输出必须逐字一致。

<a id="see-also"></a>

## 67.4 另请参阅（See also）

[系统关闭（System power off）](../power/P063_系统关机接口.md)

[唤醒控制器（WUC）](https://docs.zephyrproject.org/latest/doxygen/html/group__wuc__interface.html)

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/mcxn_a/system_off/src/main.c)；[prj.conf](../../../samples/boards/nxp/mcxn_a/system_off/prj.conf)；[tests.yaml](../../../samples/boards/nxp/mcxn_a/system_off/tests.yaml)；[mcxn.overlay](../../../samples/boards/nxp/mcxn_a/system_off/mcxn.overlay)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/mcxn_a/system_off/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/mcxn_a/system_off/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/mcxn_a/system_off/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P066_RW612低功耗Flash擦写检查.md) · [返回大纲](大纲.md) · [下一章](P068_RT1060系统关闭.md)
