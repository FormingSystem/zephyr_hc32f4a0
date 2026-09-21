---
id: learning-board-2
title: 按 PCB 连接修改设备树
kind: tutorial
status: ready
domains: [embedded, tools]
---
<!-- SPDX-License-Identifier: Apache-2.0 -->

# 2. 按 PCB 连接修改设备树

上一章选好了板与软件能力，应用却还需要知道“这块板的灯接在哪里”。GPIO 驱动能工作，不等于它知道你的 PCB。设备树把这类连接描述交给构建系统，再生成驱动可使用的数据。

本章只改变应用选择哪颗已经接好的 LED。随后用一个非法引脚值观察约束如何拒绝配置。这样能学到修改方式，又不会把未经核实的脚号写成可用的移植方案。

## 2.1 从电路信号到软件属性

真正换 PCB 时，先建立“器件信号→芯片物理脚号→端口与位号→复用功能→电气条件”的对应。PA9 是 A 端口第 9 位，不是芯片封装第 9 脚；字段叫 pin，也不保证它接受物理脚号。

本板实装 HC32F4A0PITB，LQFP100、12 MHz 晶振；blue_led 使用 PD10，green_led 使用 PE15，均低有效。芯片封装缺失引脚按 NC 处理。这里沿用项目已核实映射，不另猜一组“看起来空闲”的脚。

文件分工可以从一次构建理解：芯片 .dtsi 提供可复用外设描述，板 .dts 组合实装连接，应用 overlay 叠加这次构建的改动，binding 约束属性类型和值，驱动最后使用生成数据。**overlay** 是修改文件，**binding** 是属性规则，两者不是不同名字的同一份设备树。

## 2.2 先读当前 LED 描述

板 .dts 中与本实验有关的完整节点如下，外围板文件还包含其他硬件：

```dts
leds {
    compatible = "gpio-leds";
    blue_led: led-0 {
        gpios = <&gpiod 10 GPIO_ACTIVE_LOW>;
        label = "LED3 blue";
    };
    green_led: led-1 {
        gpios = <&gpioe 15 GPIO_ACTIVE_LOW>;
        label = "LED4 green";
    };
};
aliases {
    led0 = &blue_led;
    led1 = &green_led;
};
```

blue_led、green_led 是节点标签，& 表示引用；led-0、led-1 是节点名字。gpios 中依次是控制器引用、控制器内位号和标志：&gpioe 15 指 PE15，GPIO_ACTIVE_LOW 说明逻辑有效对应低电平。

aliases 给应用一个不必绑定具体器件名的入口。应用使用 led0，板描述目前让它对应蓝灯。只改变别名，就能保持应用代码不动而选择另一颗已定义 LED。chosen 则用于控制台等系统指定用途，不能把所有引用都放进 aliases 代替。

## 2.3 让这一次构建选择绿灯

承接上一章，.venv 已准备，board-textbook 已存在；命令继续从仓库根目录执行。先复制 overlay 原件：

```bash
cp learning/board/labs/green-led.overlay build/learning-tools/board-textbook/green-led.overlay
cat build/learning-tools/board-textbook/green-led.overlay
```

其全部有效内容为：

```dts
/ {
    aliases {
        led0 = &green_led;
    };
};
```

/ 表示根节点，aliases 在它下面。这里没有重新定义 GPIO，也没有增加驱动，只覆盖 led0 的目标。配置与构建：

```bash
python scripts/project_env.py exec cmake -S samples/bringup -B build/learning-tools/board-textbook/green -G Ninja -DBOARD=uyup_rpi_a/hc32f4a0pitb -DEXTRA_CONF_FILE=../../build/learning-tools/board-textbook/debug.conf -DDTC_OVERLAY_FILE=../../build/learning-tools/board-textbook/green-led.overlay
python scripts/project_env.py exec cmake --build build/learning-tools/board-textbook/green
rg -n -A 7 "aliases|green_led|blue_led" build/learning-tools/board-textbook/green/zephyr/zephyr.dts
```

DTC_OVERLAY_FILE 按应用源码目录解析，路径规则与上一章 EXTRA_CONF_FILE 相同。构建目录采用 green，避免混淆上一章的默认树。

生成的 zephyr.dts 中，led0 应对应 /leds/led-1；工具可能将标签引用解析成节点路径，不一定保留输入中的字面写法。查看对应节点，gpios 仍指 PE15、低有效。我们验证的是最终树和编译结果；尚未烧录，因此不能声称已经看到绿灯闪烁。

## 2.4 自己写一个相反选择，再比较

在复制品目录新建 blue-led.overlay，完整内容如下。用 Bash 写入时，DTS 结束标记必须独占一行：

```bash
cat > build/learning-tools/board-textbook/blue-led.overlay <<'DTS'
/ {
    aliases {
        led0 = &blue_led;
    };
};
DTS
python scripts/project_env.py exec cmake -S samples/bringup -B build/learning-tools/board-textbook/blue -G Ninja -DBOARD=uyup_rpi_a/hc32f4a0pitb -DDTC_OVERLAY_FILE=../../build/learning-tools/board-textbook/blue-led.overlay
python scripts/project_env.py exec cmake --build build/learning-tools/board-textbook/blue
rg -n -A 5 "aliases" build/learning-tools/board-textbook/blue/zephyr/zephyr.dts
```

led0 应恢复对应 /leds/led-0。两个构建目录同时保留，能直接比较，避免靠记忆猜刚才选中了谁。修改生成的 zephyr.dts 不能作为长期输入，下一次生成可能覆盖它。

长期同一 PCB 的共同接线放板 .dts，一次应用选择可放 overlay；新 PCB 型号差异很大时应建立独立板身份，而不是永久伪装成旧板。芯片寄存器与封装限制则属于芯片描述层。

## 2.5 合法属性也不保证驱动支持所有映射

真正换 UART 引脚还要核对复用功能。许多 SoC 使用 pinctrl 描述引脚复用状态，其宏、binding 与驱动都依平台而定；不能把另一芯片的例子直接抄到 HC32。

本仓库当前 USART1 使用 PA9 TX、PA10 RX，板文件的相关配置是：

```dts
&usart1 {
    status = "okay";
    current-speed = <115200>;
    tx-port = <&gpioa>;
    tx-pin = <9>;
    rx-port = <&gpioa>;
    rx-pin = <10>;
};
```

status 让节点启用，仍需 Kconfig/CMake 把驱动纳入。xhsc,hc32-uart.yaml 允许位号 0..15；当前 uart_hc32.c 实现则进一步限定实例与这组引脚，不匹配时返回 -ENOTSUP。也就是说，某个 0..15 的值可能通过属性检查，运行时仍不受驱动支持。

先用越界值观察更早的检查。材料 invalid-uart.overlay 的完整有效内容是：

```dts
&usart1 {
    tx-pin = <16>;
};
```

复制并配置：

```bash
cp learning/board/labs/invalid-uart.overlay build/learning-tools/board-textbook/invalid-uart.overlay
python scripts/project_env.py exec cmake -S samples/bringup -B build/learning-tools/board-textbook/invalid -G Ninja -DBOARD=uyup_rpi_a/hc32f4a0pitb -DDTC_OVERLAY_FILE=../../build/learning-tools/board-textbook/invalid-uart.overlay
echo $?
```

预期配置阶段因 tx-pin=16 不符合枚举而失败，不应等到 C 编译。这不是“设备树坏了”的笼统结论，错误应具体指向这个属性和值。

在同一构建目录明确改回正确输入：

```bash
python scripts/project_env.py exec cmake -S samples/bringup -B build/learning-tools/board-textbook/invalid -G Ninja -DBOARD=uyup_rpi_a/hc32f4a0pitb -DDTC_OVERLAY_FILE=../../build/learning-tools/board-textbook/blue-led.overlay
python scripts/project_env.py exec cmake --build build/learning-tools/board-textbook/invalid
```

应恢复成功。不要放宽 binding 来容忍这次人为越界，也不要只编辑 overlay 文件名却忘了更新缓存中的配置参数。

## 2.6 适配需要沿着哪条链核对

原理图与封装决定可用连接；设备树表达连接；binding 检查属性；驱动决定如何配置寄存器；实板电平、收发与时序才检验真实硬件。语法合法、驱动支持、电气正确是三个不同判断。

增加新 UART 映射时，先查芯片复用表、封装和 PCB，再修改驱动的配置处理，必要时扩展 binding 或实现 pinctrl，最后做构建与实板测试。GPIO 例子编译成功不代表时钟、Flash 等待周期和供电也全部正确。

本章练习已经只改变一个 alias，另一次只改变非法位号。试着解释两次实验分别检查了哪一层，为什么都不能替代示波器或串口收发观察。下一章用模拟器验证软件行为，同时继续保留这个边界。

[设备树操作依据](https://docs.zephyrproject.org/latest/build/dts/howtos.html) · [上一章](P01_选择目标板与软件配置.md) · [下一章](P03_用Twister和QEMU验证配置.md)
