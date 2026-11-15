---
id: learning.zephyr-docs.testing.test-bsim
title: BabbleSim测试
kind: reference
status: maintained
domains: [zephyr, testing]
source_url: https://docs.zephyrproject.org/latest/develop/test/bsim.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第5章\_BabbleSim测试

原文：[BabbleSim](https://docs.zephyrproject.org/latest/develop/test/bsim.html)。读取日期：2026-10-12，`latest`。

## 5.1\_BabbleSim与Zephyr

Zephyr 使用 **BabbleSim（无线物理层仿真器）**测试部分无线协议，包括**低功耗蓝牙（Bluetooth Low Energy，Bluetooth LE）**协议栈、IEEE 802.15.4，以及部分网络协议栈。

BabbleSim 提供**物理层（Physical Layer，PHY）**仿真，与 Zephyr 的 [bsim开发板模型](../bsim_reference/P001_Bsim开发板设计.md#bsim-boards)配合，可模拟多个蓝牙 LE 或 802.15.4 设备组成的网络。以 bsim 板为目标构建时，产物是包含应用、Zephyr 操作系统和硬件模型的 Linux 可执行程序；发生无线活动时，它连接 BabbleSim PHY 仿真以模拟无线信道。

仿真器的[获取](https://babblesim.github.io/fetching.html)与[构建](https://babblesim.github.io/building.html)方法见 [BabbleSim文档](https://BabbleSim.github.io)。具体板的构建和例子见 [nrf52_bsim](../bsim_reference/P002_NRF52模拟开发板.md#nrf52-bsim)、[nrf5340bsim](../bsim_reference/P003_NRF5340模拟开发板.md#nrf5340bsim)、[nrf54l15bsim](../bsim_reference/P004_NRF54L15模拟开发板.md#nrf54l15bsim)。

> 译注：IEEE 802.15.4 是无线个人区域网络相关标准名称；这里使用的是仿真硬件模型，不能将 Linux 仿真结果视为同名真实芯片的射频或实板验证。

## 5.2\_两类测试

是否包含无线活动，决定测试能否作为单个进程运行，还是需要同时启动物理层与多台模拟设备。

### 5.2.1\_没有无线活动的测试

bsim 板不发生无线活动时，无需连接物理层仿真。因此可像 `native_sim` 一样与 Twister 配合，运行标准 Zephyr 测试；区别在于 bsim 使用真实 **片上系统（System on Chip，SoC）**的硬件模型及相应驱动。

### 5.2.2\_包含无线活动的测试

此类测试至少需要运行物理层仿真，通常还需要不止一个模拟设备。因此每个测试有专用脚本，按所需参数启动各设备、物理层可执行程序以及其他工具。通过 Twister 执行时，应使用 [BabbleSim支撑程序](../twister/P014_BabbleSim支撑程序.md)。测试保存在官方 [tests/bsim/](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/bsim/) 目录。

主要分为两组：

- **自检嵌入式应用测试（Self-checking Embedded Application Test）**：部分模拟设备的应用内置检查，判断测试通过或失败。它们通过 `bs_tests` 系统报告结果，通常还能把多个测试编进同一二进制。详情见 [bs_tests说明](../bsim_reference/P001_Bsim开发板设计.md#bsim-boards-bs-tests)。
- 使用 [EDTT测试工具](https://github.com/EDTTool/EDTT)的测试：Python 测试通过**远程过程调用（Remote Procedure Call，RPC）**控制嵌入式应用并判定结果。原文说明这类测试已包含相当一部分蓝牙资格认证测试套件。

不同测试类型与板模型的关系见 [bsim板测试说明](../bsim_reference/P001_Bsim开发板设计.md#bsim-boards-tests)。

## 5.3\_覆盖率

bsim 板基于 **可移植操作系统接口架构（Portable Operating System Interface Architecture，POSIX Architecture）**，便于收集**代码覆盖率（Code Coverage）**。给 Twister 加 `--coverage`，会自动启用 Kconfig 选项 `CONFIG_COVERAGE` 并生成覆盖率报告，详细流程见 [测试覆盖率](P003_测试覆盖率.md)。

## 5.4\_构建与运行

先按 [nrf52_bsim构建运行说明](../bsim_reference/P002_NRF52模拟开发板.md#nrf52bsim-build-and-run)准备仿真器，再使用 Twister 构建和执行。多设备测试需传 `--fixture bsim_multi_test`，声明所需仿真测试装置。

原文从 `${ZEPHYR_BASE}`，即所用 Zephyr 源码根执行以下蓝牙测试：

```sh
twister -p nrf52_bsim/native -T tests/bsim/bluetooth/host/adv/chain/ --fixture bsim_multi_test
```

> 译注：命令采用 Linux Bash。原文使用环境已就绪时可找到的 `twister` 入口；也可按前面运行器章节使用相同选项的 `west twister`。`bsim_multi_test` 是装置名称，不是实际串接多块硬件的命令。本次没有安装仿真器或执行测试。

二进制已构建后，可直接调用单项脚本：

```sh
BOARD=nrf52_bsim/native tests/bsim/bluetooth/host/adv/chain/tests_scripts/adv_chain.sh
```

此处 `BOARD` 是传给这次脚本调用的平台变量。调试问题时，Twister 的 `-n` / `--no-clean`、`--aggressive-no-clean`、`-b` / `--build-only` 常有帮助，其复用和省略阶段的区别见 [命令行选项](../twister/P002_Twister命令行选项.md)。

## 5.5\_旧式批处理脚本

在 Twister 增加 bsim 支撑程序前，多设备测试依赖 `tests/bsim/compile.sh` 与 `run_parallel.sh`，供 **持续集成（Continuous Integration，CI）**及用户批量构建、执行。它们仍可使用，但原文建议转向 Twister 与 `tests.yaml` 定义。

这些脚本需要若干环境变量。下面从 Zephyr 源码根构建并执行全部测试；`ZEPHYR_BASE` 是源码根变量，`RESULTS_FILE` 指定结果文件，`SEARCH_PATH` 指定寻找运行脚本的目录：

```sh
# Build all the tests
${ZEPHYR_BASE}/tests/bsim/compile.sh

# Run them (in parallel)
RESULTS_FILE=${ZEPHYR_BASE}/myresults.xml \
   SEARCH_PATH=${ZEPHYR_BASE}/tests/bsim \
      ${ZEPHYR_BASE}/tests/bsim/run_parallel.sh
```

只构建和执行蓝牙主机广播测试子集时：

```sh
# Build the Bluetooth host advertising tests
${ZEPHYR_BASE}/tests/bsim/bluetooth/host/adv/compile.sh

# Run them (in parallel)
RESULTS_FILE=${ZEPHYR_BASE}/myresults.xml \
   SEARCH_PATH=${ZEPHYR_BASE}/tests/bsim/bluetooth/host/adv \
      ${ZEPHYR_BASE}/tests/bsim/run_parallel.sh
```

更多批处理选项与例子见 `run_parallel.sh` 自带帮助。所需二进制已经生成后，也可直接运行单项测试。例如先通过 `WORK_DIR` 指定本次编译工作目录，构建网络测试：

```sh
WORK_DIR=${ZEPHYR_BASE}/bsim_out ${ZEPHYR_BASE}/tests/bsim/net/compile.sh
```

再调用其中的 IEEE 802.15.4 回显测试：

```sh
${ZEPHYR_BASE}/tests/bsim/net/sockets/echo_test/tests_scripts/echo_test_802154.sh
```

> 译注：这些是原文旧脚本例子，当前源码版本是否仍保留对应入口应先核对；没有实际生成 `myresults.xml` 或运行这些脚本。变量赋值与命令处于同一行时，只向该次程序调用传递对应值。

## 5.6\_测试代码与脚本约定

测试代码遵循官方 [蓝牙示例测试约定](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/bsim/bluetooth/host/misc/sample_test/README.rst)。脚本应沿用现有方式，不另建只服务单个测试的 Python 运行器或另一层 Shell 抽象；统一变量和执行形式，便于维护者进行全树构建或兼容性更新。

有通用改进时，原文建议通过**拉取请求（Pull Request，PR）**同步改进相关脚本，或先以**征求意见提案（Request for Comments，RFC）**、BabbleSim 社区讨论沟通方案。以下划线 `_` 开头的脚本不会自动发现和运行，可用于共享辅助函数或本地开发、构建、调试工具。

脚本应遵循以下完整约定：

1. 每个测试由 `tests_scripts/` 子目录中的 `.sh` 文件定义。
2. 推荐每个文件只运行一个测试，便于 CI 并行。
3. 假定所需二进制已构建，运行脚本自身不编译它们。
4. 启动全部模拟设备进程和物理层仿真进程。
5. 测试通过返回退出码 0，失败返回非零。
6. 每个测试使用唯一的**仿真标识（Simulation ID）**，以便多个测试并行。
7. 脚本和镜像只在 `${BSIM_OUT_PATH}/results/<simulation_id>/` 或系统 `/tmp/` 临时目录内修改文件，不在工作站留下散落文件。`BSIM_OUT_PATH` 是 BabbleSim 输出根变量。
8. 若测试需要连续多个仿真阶段，例如配对、断电、重新上电，每段使用不同仿真标识，方便事后分别检查无线活动。
9. 避免过长测试。超过 20 秒时，考虑拆成多个独立测试。
10. 超过 5 秒时，将执行超时变量 `EXECUTE_TIMEOUT` 至少设为测得运行时间的五倍；不要把它设得低于默认值。
11. 输出应少于约一百行。可以充分使用日志宏 `LOG_DBG()`，但不要默认开启调试等级 `DBG`。
12. 使用物理层仿真的脚本，应把收到的额外参数直接转发给 PHY 可执行程序。例如 `-c` **检查模式（Check Mode）**验证本次与上次仿真产生完全相同的无线流量。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：基准测试框架](P004_基准测试框架.md) · [本模块主线目录](../reading/testing.md) · [全部主线](../reading/README.md) · [下一篇：持续集成测试计划选择器](P006_持续集成测试计划选择器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：基准测试框架](P004_基准测试框架.md) · [下一章：持续集成测试计划选择器](P006_持续集成测试计划选择器.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
