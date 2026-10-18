---
id: learning.zephyr-docs.twister.harness-bsim
title: BabbleSim支撑程序
kind: reference
status: maintained
domains: [zephyr, twister]
source_url: https://docs.zephyrproject.org/latest/develop/twister/harness/bsim.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第14章\_BabbleSim支撑程序

原文：[Bsim](https://docs.zephyrproject.org/latest/develop/twister/harness/bsim.html)。读取日期：2026-10-12，`latest`。

`bsim` **测试支撑程序（Harness）**扩展 [脚本支撑程序](P013_脚本支撑程序.md)，用于执行 **BabbleSim（多设备仿真环境）**测试。

构建阶段，它把构建目录中的最终可执行文件 `zephyr.exe` 复制到 `${BSIM_OUT_PATH}/bin`；`BSIM_OUT_PATH` 是 BabbleSim 输出根目录变量。运行阶段，执行 `tests_scripts` 中列出的脚本。

## 14.1\_可执行文件命名

默认名字为 `bs_<platform_name>_<test_path>_<test_scenario_name>`，将点号和斜线替换为下划线，分别编码平台、测试路径及场景名。

可用 `harness_config.bsim_exe_name` 覆盖后两部分。设置后复制出的文件名为 `bs_<platform_name>_<bsim_exe_name>`，而不是按测试路径与场景自动形成。

## 14.2\_多镜像测试例子

下例的构建变量 `CONF_FILE` 选择应用 Kconfig 配置文件。以下原例中，**广播者（Advertiser）**只构建，**扫描者（Scanner）**通过 `required_applications` 声明依赖它，并由脚本启动仿真测试。这两个名称是蓝牙广播通信中发送广播与接收扫描的角色。

```yaml
common:
  platform_allow:
    - nrf52_bsim/native
  harness: bsim
tests:
  bluetooth.host.adv.extended.advertiser:
    build_only: true
    harness_config:
      bsim_exe_name: tests_bsim_bluetooth_host_adv_extended_prj_advertiser_conf
    extra_args:
      CONF_FILE=prj_advertiser.conf
  bluetooth.host.adv.extended.scanner:
    harness_config:
      bsim_exe_name: tests_bsim_bluetooth_host_adv_extended_prj_scanner_conf
      tests_scripts:
        - tests_scripts/run_adv_extended.sh
    extra_args:
      CONF_FILE=prj_scanner.conf
    required_applications:
      - application: bluetooth.host.adv.extended.advertiser
```

`CONF_FILE` 是选择应用 Kconfig 配置文件的构建变量。两个 `bsim_exe_name` 使广播者、扫描者产物有不同名字；`tests_scripts/run_adv_extended.sh` 是执行脚本路径。Twister 先完成依赖应用构建，再允许依赖它的场景执行，详细规则见 [Twister测试运行器](P001_Twister测试运行器.md)。

> 译注：`nrf52_bsim/native` 是原例仿真目标，不代表为真实 nRF52 或 HC32 硬件生成可直接烧录的镜像。本例需要对应 BabbleSim 环境、脚本和配置文件已存在。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：脚本支撑程序](P013_脚本支撑程序.md) · [本模块主线目录](../reading/twister.md) · [全部主线](../reading/README.md) · [下一篇：Shell支撑程序](P015_Shell支撑程序.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：脚本支撑程序](P013_脚本支撑程序.md) · [下一章：Shell支撑程序](P015_Shell支撑程序.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
