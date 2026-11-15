---
id: learning.zephyr-docs.external_modules.page-19
title: ExecuTorch
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/executorch.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="executorch"></a>
<a id="external-module-executorch"></a>

# 第19章\_ExecuTorch

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/executorch.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 19.1\_简介（Introduction）

[ExecuTorch](https://github.com/pytorch/executorch) 是PyTorch的设备端推理运行时（On-device Inference Runtime）。在Zephyr中可作为外部模块，使用CPU或Arm Ethos-U神经处理单元（Neural Processing Unit，NPU）运行模型。

初次接触时可先阅读 [ExecuTorch工作方式](https://docs.pytorch.org/executorch/stable/intro-how-it-works.html)与 [入门架构概览](https://docs.pytorch.org/executorch/stable/getting-started-architecture.html)。ExecuTorch采用 [BSD三条款许可证](https://github.com/pytorch/executorch/blob/main/LICENSE)。

<a id="usage-with-zephyr"></a>

> 译注——文档版本：原文的ExecuTorch模块和Python包固定为1.4.0；上面的stable文档入口在本次复核时已显示1.5。阅读工作方式可沿用入口，复制接口和模型导出参数时应核对与实际安装版本对应的文档。

## 19.2\_在Zephyr中使用（Usage with Zephyr）

本节覆盖模块注册、模型准备，以及CPU和Arm Ethos-U NPU两条路径的构建／运行步骤。

**前提：**

- ExecuTorch工具要求Python 3.12–3.13，可使用独立虚拟环境，或以兼容Python版本创建的Zephyr虚拟环境。
- 只有选择Corstone固定虚拟平台（Fixed Virtual Platform，FVP），例如 `mps3/corstone300/fvp`，模拟Cortex-M与Ethos-U而不使用硬件时，才需要Arm FVP；安装见[下文FVP安装](#fvp-install)。
- macOS通过 [FVPs-on-Mac](https://github.com/Arm-Examples/FVPs-on-Mac.git) 执行NPU推理路径时才需要Docker。

<a id="installing-executorch"></a>

### 19.2.1\_安装ExecuTorch（Installing ExecuTorch）

步骤1：把ExecuTorch注册为外部模块。可新建 `zephyrproject/zephyr/submanifests/executorch.yaml`，或将项目条目合并到已有应用 `west.yml`：

```yaml
manifest:
  projects:
    - name: executorch
      url: https://github.com/pytorch/executorch
      revision: v1.4.0
      path: modules/lib/executorch
      submodules: true
```

步骤2：运行west更新：

```bash
west update
```

步骤3：安装带Arm Ethos-U依赖的ExecuTorch。在使用Python 3.12–3.13的Zephyr虚拟环境内执行：

```bash
pip install "executorch[ethos_u]==1.4.0"
```

`ethos_u`附加依赖（Extra）会安装所需Arm后端工具，包括张量算子集架构（Tensor Operator Set Architecture，TOSA）工具及Ethos-U Vela编译器。

<a id="build-and-run"></a>

### 19.2.2\_构建与运行（Build and run）

嵌入式AI模型可使用专用NPU加速。Arm的 [Ethos-U NPU系列](https://www.arm.com/products/silicon-ip-cpu?families=ethos%20npus)面向高效设备端推理。下文保留原页的两条分支：Arm Ethos-U NPU推理与纯CPU推理。

<a id="tab-0-QXJtIEV0aG9zLVUgTlBVIEluZmVyZW5jZQ=="></a>
<a id="panel-0-QXJtIEV0aG9zLVUgTlBVIEluZmVyZW5jZQ=="></a>

#### 19.2.2.1\_Arm\_Ethos-U\_NPU推理

<a id="fvp-install"></a>

##### 19.2.2.1.1\_安装Arm\_FVP（Installing Arm FVPs）

FVP是Arm提供的模拟器，可在没有物理硬件时运行Zephyr。原文在这里并列Ethos-U55、U65、U85，并称通过Corstone-300参考平台模拟。

> 译注——目标组合：后续实际模型选项是 `ethos-u55-128`，应与具体FVP配置一致。原文并列多个NPU名称，不能据此推定一个Corstone-300配置支持所有型号；安装包和目标组合按对应Arm平台说明选择。

<a id="tab-1-VWJ1bnR1"></a>
<a id="panel-1-VWJ1bnR1"></a>

**Ubuntu分支**

步骤1：从 [Arm Corstone FVP下载页](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)取得Corstone-300安装包。可安装在机器上自行选择的位置，无须放在Zephyr工程目录内。版本号随发布变化，以下文件名和URL需按选定版本设置：

```bash
FVP_TGZ="FVP_Corstone_SSE-300_11.27_42_Linux64_armv8l.tgz"
FVP_URL="https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Corstone-IoT/Corstone-300/${FVP_TGZ}"
curl -L -o "${FVP_TGZ}" "${FVP_URL}"
```

> 译注——主机架构：原包名中的 `Linux64_armv8l` 和后续路径属于该Linux主机平台版本，不是目标微控制器型号。下载前需选择与自己的主机匹配的包，不能对所有Ubuntu主机直接套用这一文件名。

步骤2：解压下载的归档：

```bash
tar -xf "${FVP_TGZ}"
```

步骤3：运行安装脚本：

```bash
./FVP_Corstone_SSE-300.sh --i-agree-to-the-contained-eula --no-interactive -q
```

> 译注——参数含义：原命令显式包含接受安装包许可、非交互安装与安静输出选项；这里仅保留原文，没有运行安装器。

步骤4：把FVP加入命令搜索路径（PATH）。`FVP_Corstone_SSE-300_Ethos-U55` 与 `FVP_Corstone_SSE-300_Ethos-U65` 位于同一目录：

```bash
export PATH=$HOME/FVP_Corstone_SSE-300/models/Linux64_armv8l_GCC-9.3:$PATH
```

步骤5：加载随附脚本，安装所需运行依赖 `libpython3.9.so.1.0`。不同Shell的方式略有不同。

bash：

```bash
source $HOME/FVP_Corstone_SSE-300/scripts/runtime.sh
unset PYTHONHOME
```

zsh不会自动填充 `BASH_SOURCE`，需在加载前手工设置：

```zsh
BASH_SOURCE=$HOME/FVP_Corstone_SSE-300/scripts/runtime.sh
source $HOME/FVP_Corstone_SSE-300/scripts/runtime.sh
unset PYTHONHOME
```

步骤6：验证安装：

```bash
FVP_Corstone_SSE-300_Ethos-U55 --version
FVP_Corstone_SSE-300_Ethos-U65 --version
```

<a id="tab-1-bWFjT1M="></a>
<a id="panel-1-bWFjT1M="></a>

**macOS分支**

macOS通过 [FVPs-on-Mac](https://github.com/Arm-Examples/FVPs-on-Mac.git) 提供的Docker包装器运行FVP。

步骤1：克隆仓库并切换到指定提交。仓库可放在自行选择的位置，无须位于Zephyr工程内：

```bash
git clone https://github.com/Arm-Examples/FVPs-on-Mac.git
```

```bash
cd FVPs-on-Mac
git switch --detach 1458860
```

步骤2：构建Docker包装器：

```bash
./build.sh
```

**注意：**构建包装器及执行FVP命令之前，Docker必须已经安装并处于运行状态。

步骤3：基本检查：

```bash
./bin/FVP_Corstone_SSE-300 --version
```

步骤4：将FVP可执行程序加入当前环境：

```bash
export PATH=$PATH:$(pwd)/bin
```

<a id="tab-1-V2luZG93cw=="></a>
<a id="panel-1-V2luZG93cw=="></a>

**Windows分支**

步骤1：在 [Arm FVP下载页](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)选择Windows安装器并按向导安装。位置可自行选择，不必在Zephyr工程内。原文给出的典型工具目录是 `C:\Program Files\ARM\FVP_Corstone_SSE-300\models\Win64_VC2019`。

> 译注——目录性质：这是官方工具安装目录的示例，不是读者仓库必须位于C盘的要求。后续以自己的实际安装位置找到可执行程序。

**注意：**如果没有 `python39.dll`，可能还需要安装它。

步骤2：打开新的PowerShell窗口，进入实际FVP可执行程序目录并检查：

```powershell
.\FVP_Corstone_SSE-300.exe --version
```

<a id="tab-1-WmVwaHlyIERvY2tlciBDSQ=="></a>
<a id="panel-1-WmVwaHlyIERvY2tlciBDSQ=="></a>

**Zephyr Docker CI分支**

[Zephyr Docker持续集成（Continuous Integration，CI）镜像](https://github.com/zephyrproject-rtos/docker-image)是手工安装的替代方案。原文说明该官方容器包含Corstone-300、Corstone-320 FVP及其他Zephyr构建依赖，无须另装FVP。

步骤1：拉取镜像：

```bash
docker pull ghcr.io/zephyrproject-rtos/zephyr-build:main
```

步骤2：启动容器，挂载Zephyr工作区和Zephyr SDK：

```bash
docker run -it --rm \
  -v $HOME/zephyrproject:$HOME/zephyrproject \
  -v $HOME/zephyr-sdk-0.17.4:$HOME/zephyr-sdk-0.17.4 \
  -w $HOME/zephyrproject \
  -e HOME=$HOME \
  -e ZEPHYR_SDK_INSTALL_DIR=$HOME/zephyr-sdk-0.17.4 \
  --user root \
  --entrypoint /bin/bash \
  ghcr.io/zephyrproject-rtos/zephyr-build:main
```

**注意：**SDK版本 `0.17.4` 可能变化，应换成已安装版本，或使用下列通用形式：

```bash
docker run -it --rm \
  -v $HOME/zephyrproject:$HOME/zephyrproject \
  -v $HOME/zephyr-sdk-<version>:$HOME/zephyr-sdk-<version> \
  -w $HOME/zephyrproject \
  -e HOME=$HOME \
  -e ZEPHYR_SDK_INSTALL_DIR=$HOME/zephyr-sdk-<version> \
  --user root \
  --entrypoint /bin/bash \
  ghcr.io/zephyrproject-rtos/zephyr-build:main
```

> 译注——占位符：执行前把 `<version>` 换成具体版本；它不是Shell可直接解释的文字。工作区和SDK的挂载位置由读者自己的目录决定。这里的 `$HOME` 是当前环境变量，不是作者固定的仓库路径。

步骤3：在容器内激活Zephyr虚拟环境：

```bash
source $HOME/zephyrproject/.venv/bin/activate
```

> 译注——环境平台：这条激活命令使用Linux虚拟环境的 `bin/activate`。挂载的工作区若只有Windows创建的虚拟环境，应先准备适合容器平台的环境，不能认为挂载后即可跨系统复用。

步骤4：检查FVP可用性：

```bash
FVP_Corstone_SSE-300 --version
FVP_Corstone_SSE-320 --version
```

随后可在容器内执行下面的west构建命令。

##### 19.2.2.1.2\_准备Ethos-U55\_PTE模型（Prepare the Ethos-U55 PTE model）

`.pte` 是ExecuTorch序列化程序（Serialized Program）文件，也是把PyTorch模型部署到边缘和移动设备的最终二进制格式。自有模型导出及Arm Ethos-U后端转换（Lowering）见 [ExecuTorch导出指南](https://docs.pytorch.org/executorch/stable/using-executorch-export.html)。

本例用最小加法模型，将两个张量（Tensor）逐元素相加，只用于验证从模型编译到设备端NPU推理的完整流程。预期每个元素为`2 + 2 = 4`。

从原文所称的Zephyr根位置，例如 `~/zephyrproject`，执行以下相应系统分支。

<a id="tab-2-VWJ1bnR1L21hY09T"></a>
<a id="panel-2-VWJ1bnR1L21hY09T"></a>

Ubuntu／macOS：

```bash
cd ~/zephyrproject
python -m executorch.backends.arm.scripts.aot_arm_compiler \
  --model_name=modules/lib/executorch/examples/arm/example_modules/add.py \
  --quantize --delegate --target=ethos-u55-128 --output=add_u55_128.pte
```

<a id="tab-2-V2luZG93cw=="></a>
<a id="panel-2-V2luZG93cw=="></a>

Windows PowerShell：

```powershell
cd ~/zephyrproject
python -m executorch.backends.arm.scripts.aot_arm_compiler `
  --model_name=modules/lib/executorch/examples/arm/example_modules/add.py `
  --quantize --delegate --target=ethos-u55-128 --output=add_u55_128.pte
```

`--delegate` 指示 `aot_arm_compiler` 使用Ethos-U后端；`--target=ethos-u55-128` 选择Ethos-U变体及乘加（Multiply-Accumulate，MAC）数量，必须与硬件或FVP配置匹配。

> 译注——工作区根与源码根：原命令中的 `modules/lib/executorch` 位于west工作区根下，因此这里应进入包含 `modules/` 的工作区根。它通常是Zephyr源码目录的父目录，不能只按“Zephyr root”字样进入 `zephyr/` 后继续套用相同相对路径。`~/zephyrproject`属于官方示例布局，读者应使用自己的工作区。

##### 19.2.2.1.3\_构建与运行（Build and Run）

从同一工作区位置构建并运行。

<a id="tab-3-VWJ1bnR1L21hY09T"></a>
<a id="panel-3-VWJ1bnR1L21hY09T"></a>

Ubuntu／macOS：

```bash
cd ~/zephyrproject
west build -p auto -b mps3/corstone300/fvp \
  modules/lib/executorch/zephyr/samples/hello-executorch \
  -t run -- -DET_PTE_FILE_PATH=add_u55_128.pte
```

<a id="tab-3-V2luZG93cw=="></a>
<a id="panel-3-V2luZG93cw=="></a>

Windows PowerShell：

```powershell
cd $env:USERPROFILE\zephyrproject
west build -p auto -b mps3/corstone300/fvp `
  modules/lib/executorch/zephyr/samples/hello-executorch -t run -- `
  "-DET_PTE_FILE_PATH=$PWD\add_u55_128.pte"
```

> 译注——模型相对路径依据：本例固定版本v1.4.0的[示例CMakeLists.txt](https://raw.githubusercontent.com/pytorch/executorch/v1.4.0/zephyr/samples/hello-executorch/CMakeLists.txt)把相对 `ET_PTE_FILE_PATH` 按示例源码目录 `CMAKE_CURRENT_SOURCE_DIR` 解析，而非终端当前目录。若PTE仍位于工作区根，原Unix命令仅传文件名会找错位置；可改传从示例目录到它的相对路径，例如 `../../../../../../add_u55_128.pte`，或将文件放入示例目录后使用文件名。Windows原例通过运行时 `$PWD` 形成实际位置，未固定作者目录。后面的CPU模型也适用同一规则。

<a id="tab-0-Q1BVLW9ubHkgSW5mZXJlbmNl"></a>
<a id="panel-0-Q1BVLW9ubHkgSW5mZXJlbmNl"></a>

#### 19.2.2.2\_纯CPU推理

##### 19.2.2.2.1\_准备模型（Prepare the model）

本例是为Cortex-M55导出的最小加法模型，使用当前Arm提前编译（Ahead-of-Time，AOT）编译器提供的纯CPU目标。支持的目标可能变化；如果运行时支持所需算子（Operator），部分其他Cortex-M板也可能运行生成的 `.pte`，但兼容性应逐板验证。从同一工作区根执行：

```bash
python -m executorch.backends.arm.scripts.aot_arm_compiler \
  --model_name=modules/lib/executorch/examples/arm/example_modules/add.py \
  --quantize --target=cortex-m55 --output=add_m55.pte
```

##### 19.2.2.2.2\_构建与运行（Build and Run）

将 `<board>` 替换为目标板。原文下面列出的验证板之外，需要在实际目标确认兼容性：

```bash
west build -b <board> modules/lib/executorch/zephyr/samples/hello-executorch \
  -t run -- -DET_PTE_FILE_PATH=add_m55.pte
```

**原文说明：**以下开发板曾用同一个 `add_m55.pte` 产物测试。

STM Nucleo-N657X0-Q（`nucleo_n657x0_q`）：

```bash
west build -b nucleo_n657x0_q \
  modules/lib/executorch/zephyr/samples/hello-executorch \
  -- -DET_PTE_FILE_PATH=add_m55.pte
```

nRF5340 DK（`nrf5340dk/nrf5340/cpuapp`）：

```bash
west build -b nrf5340dk/nrf5340/cpuapp \
  modules/lib/executorch/zephyr/samples/hello-executorch \
  -- -DET_PTE_FILE_PATH=add_m55.pte
```

构建后烧录到硬件：

```bash
west flash
```

> 译注——构建与运行区别：通用命令带 `-t run`，但具体实板是否提供该运行目标应按板级支持确认。上面两个实板示例仅构建，随后用west flash烧录；本批未执行上述平台测试。

<a id="expected-run-output"></a>

### 19.2.3\_预期运行输出（Expected Run Output）

```text
I [executorch:arm_executor_runner.cpp:450 main()] Model executed successfully.
I [executorch:arm_executor_runner.cpp:457 main()] Model outputs:
I [executorch:arm_executor_runner.cpp:464 main()]   output[0]: tensor scalar_type=Float numel=5
I [executorch:arm_executor_runner.cpp:481 main()]     [0] = 4.000000
I [executorch:arm_executor_runner.cpp:481 main()]     [1] = 4.000000
I [executorch:arm_executor_runner.cpp:481 main()]     [2] = 4.000000
I [executorch:arm_executor_runner.cpp:481 main()]     [3] = 4.000000
I [executorch:arm_executor_runner.cpp:481 main()]     [4] = 4.000000
I [executorch:arm_executor_runner.cpp:499 main()] SUCCESS: Program complete, exiting.
```

原文说明每个输出 `4.000000` 表明模型在设备端成功执行，每个值都是Ethos-U NPU或CPU后端通过ExecuTorch计算 `2 + 2` 的结果。

> 译注——日志对照：Model executed successfully表示模型执行成功，Model outputs是输出列表，tensor scalar_type=Float numel=5表示浮点张量含5个元素；Program complete, exiting表示程序完成并退出。源文件行号、日志与数值均为原文示例，不是本批实测。

ExecuTorch的Zephyr支持仍在开发，更多复杂示例可在 [Zephyr示例目录](https://github.com/pytorch/executorch/tree/main/zephyr/samples)跟踪。

<a id="reference"></a>

## 19.3\_参考资料（Reference）

- [ExecuTorch](https://github.com/pytorch/executorch)：PyTorch设备端推理运行时。
- [ExecuTorch工作方式](https://docs.pytorch.org/executorch/stable/intro-how-it-works.html)：流程入门。
- [入门架构](https://docs.pytorch.org/executorch/stable/getting-started-architecture.html)：高层架构概览。
- [Arm FVPs](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs)：Cortex-M与Ethos-U模拟平台。
- [FVPs-on-Mac](https://github.com/Arm-Examples/FVPs-on-Mac.git)：在macOS运行FVP的Docker包装器。
- [Arm Ethos-U NPU系列](https://www.arm.com/products/silicon-ip-cpu?families=ethos%20npus)：设备端AI推理NPU IP。
- [ExecuTorch导出指南](https://docs.pytorch.org/executorch/stable/using-executorch-export.html)：导出及后端转换。
- [Zephyr Docker CI镜像](https://github.com/zephyrproject-rtos/docker-image)：预装FVP和构建依赖。
- [hello-executorch示例](https://github.com/pytorch/executorch/tree/main/zephyr/samples/hello-executorch)：本页使用的最小Zephyr示例。


对应官方文档源码：[doc/develop/manifest/external/executorch.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/executorch.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/executorch.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。


<!-- reading-navigation:start -->

**主线阅读**

[上一篇：ESP串口烧录器](P018_ESP串口烧录器.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Greybus](P020_Greybus.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P018_ESP串口烧录器.md) · [返回大纲](大纲.md) · [下一章](P020_Greybus.md)

</details>

<!-- reading-navigation:end -->
