/*
 * Copyright (c) 2020 The ZMK Contributors
 *
 * SPDX-License-Identifier: MIT
 */

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/init.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/sys/sys_io.h>
#include <zephyr/devicetree.h>

static int pinmux_ergohaven_init(void) {
#if (CONFIG_BOARD_ERGOHAVEN)
    const struct device *p0 = DEVICE_DT_GET(DT_NODELABEL(gpio0));
#endif
    return 0;
}

SYS_INIT(pinmux_ergohaven_init, APPLICATION, CONFIG_APPLICATION_INIT_PRIORITY);
