function mainSlider() {
    var _0xe8e3x2 = {
        cs: 0,
        pause: 5000,
        duration: 750
    };
    this['init'] = function() {
        _0xe8e3x5['init']();
        _0xe8e3x3['bindControls']();
        _0xe8e3x4['bindControls']();
    };
    var _0xe8e3x3 = {
        resize: function() {
            $('#fwslider')['css']({
                height: $('#fwslider .slide')['height']()
            });
            _0xe8e3x4['position']();
        },
        bindControls: function() {
            $(window)['resize'](function() {
                _0xe8e3x3['resize']();
            });
        }
    };
    var _0xe8e3x4 = {
        position: function() {
            $('#fwslider .slidePrev, #fwslider .slideNext')['css']({
                top: $('#fwslider')['height']() / 2 - $('#fwslider .slideNext')['height']() / 2
            });
            $('#fwslider .slidePrev')['css']({
                left: 0
            });
            $('#fwslider .slideNext')['css']({
                right: 0
            });
        },
        bindControls: function() {
            $('#fwslider .slidePrev, #fwslider .slideNext')['on']('mouseover', function() {
                $(this)['animate']({
                    opacity: 1
                }, {
                    queue: false,
                    duration: 1000,
                    easing: 'easeOutCubic'
                });
            });
            $('#fwslider .slidePrev, #fwslider .slideNext')['on']('mouseout', function() {
                $(this)['animate']({
                    opacity: 0.5
                }, {
                    queue: false,
                    duration: 1000,
                    easing: 'easeOutCubic'
                });
            });
            $('#fwslider .slideNext')['on']('click', function() {
                if ($('#fwslider .slide')['is'](':animated')) {
                    return;
                };
                if ($('#fwslider .slide:eq(' + (_0xe8e3x2['cs'] + 1) + ')')['length'] <= 0) {
                    _0xe8e3x2['cs'] = 0;
                    $('#fwslider .timers .timer .progress')['stop']();
                    $('#fwslider .timers .timer:last .progress')['animate']({
                        width: '100%'
                    }, {
                        queue: false,
                        duration: _0xe8e3x2['duration'],
                        easing: 'easeOutCubic',
                        complete: function() {
                            $('#fwslider .timers .timer .progress')['css']({
                                width: '0%'
                            });
                        }
                    });
                } else {
                    _0xe8e3x2['cs']++;
                    $('#fwslider .timers .timer .progress')['stop']();
                    $('#fwslider .timers .timer:lt(' + _0xe8e3x2['cs'] + ') .progress')['animate']({
                        width: '100%'
                    }, {
                        queue: false,
                        duration: _0xe8e3x2['duration'],
                        easing: 'easeOutCubic'
                    });
                };
                _0xe8e3x5['show']();
            });
            $('#fwslider .slidePrev')['on']('click', function() {
                if ($('#fwslider .slide')['is'](':animated')) {
                    return;
                };
                if (_0xe8e3x2['cs'] <= 0) {
                    _0xe8e3x2['cs'] = $('#fwslider .slide')['index']();
                    $('#fwslider .timers .timer .progress')['stop']();
                    $('#fwslider .timers .timer .progress')['css']({
                        width: '100%'
                    });
                    $('#fwslider .timers .timer:last .progress')['animate']({
                        width: '0%'
                    }, {
                        queue: false,
                        duration: _0xe8e3x2['duration'],
                        easing: 'easeOutCubic'
                    });
                } else {
                    _0xe8e3x2['cs']--;
                    $('#fwslider .timers .timer .progress')['stop']();
                    $('#fwslider .timers .timer:gt(' + _0xe8e3x2['cs'] + ') .progress')['css']({
                        width: '0%'
                    });
                    $('#fwslider .timers .timer:eq(' + _0xe8e3x2['cs'] + ') .progress')['animate']({
                        width: '0%'
                    }, {
                        queue: false,
                        duration: _0xe8e3x2['duration'],
                        easing: 'easeOutCubic'
                    });
                };
                _0xe8e3x5['show']();
            });
        }
    };
    var _0xe8e3x5 = {
        init: function() {
            for (var _0xe8e3x6 = 0; _0xe8e3x6 < $('#fwslider .slide')['length']; _0xe8e3x6++) {
                $('<div class="timer"><div class="progress"></div></div>')['appendTo']('#fwslider .timers');
            };
            $('#fwslider .timers')['css']({
                width: ($('#fwslider .timers .timer')['length'] + 1) * 45
            });
            $('#fwslider .slide:eq(' + _0xe8e3x2['cs'] + ')')['fadeIn']({
                duration: 500,
                easing: 'swing'
            });
            $('#fwslider')['animate']({
                height: $('#fwslider .slide:first img')['height']()
            }, {
                queue: false,
                duration: 500,
                easing: 'easeInOutExpo',
                complete: function() {
                    $('#fwslider .slidePrev')['animate']({
                        left: 0
                    }, {
                        queue: false,
                        duration: 1000,
                        easing: 'easeOutCubic'
                    });
                    $('#fwslider .slideNext')['animate']({
                        right: 0
                    }, {
                        queue: false,
                        duration: 1000,
                        easing: 'easeOutCubic'
                    });
                    _0xe8e3x5['showText']();
                    _0xe8e3x4['position']();
                    _0xe8e3x3['resize']();
                    _0xe8e3x7['run']();
                    _0xe8e3x7['focus']();
                }
            });
        },
        show: function() {
            _0xe8e3x5['hideText']();
            $('#fwslider .slide:eq(' + _0xe8e3x2['cs'] + ')')['css']({
                opacity: 0,
                zIndex: 2
            })['show']()['animate']({
                opacity: 1
            }, {
                queue: false,
                duration: _0xe8e3x2['duration'],
                easing: 'swing',
                complete: function() {
                    $('#fwslider .slide:lt(' + _0xe8e3x2['cs'] + '), #fwslider .slide:gt(' + _0xe8e3x2['cs'] + ')')['css']({
                        zIndex: 0
                    })['hide']();
                    $('#fwslider .slide:eq(' + _0xe8e3x2['cs'] + ')')['css']({
                        zIndex: 1
                    });
                    _0xe8e3x5['showText']();
                    _0xe8e3x7['run']();
                }
            });
        },
        showText: function() {
            $('#fwslider .slide:eq(' + _0xe8e3x2['cs'] + ') .title')['animate']({
                opacity: 1
            }, {
                queue: false,
                duration: 300,
                easing: 'swing'
            });
            setTimeout(function() {
                $('#fwslider .slide:eq(' + _0xe8e3x2['cs'] + ') .description')['animate']({
                    opacity: 1
                }, {
                    queue: false,
                    duration: 300,
                    easing: 'swing'
                });
            }, 150);
            setTimeout(function() {
                $('#fwslider .slide:eq(' + _0xe8e3x2['cs'] + ') .readmore')['animate']({
                    opacity: 1
                }, {
                    queue: false,
                    duration: 300,
                    easing: 'swing'
                });
            }, 300);
        },
        hideText: function() {
            $('#fwslider .slide .title')['animate']({
                opacity: 0
            }, {
                queue: false,
                duration: 300,
                easing: 'swing'
            });
            setTimeout(function() {
                $('#fwslider .slide .description')['animate']({
                    opacity: 0
                }, {
                    queue: false,
                    duration: 300,
                    easing: 'swing'
                });
            }, 150);
            setTimeout(function() {
                $('#fwslider .slide .readmore')['animate']({
                    opacity: 0
                }, {
                    queue: false,
                    duration: 300,
                    easing: 'swing'
                });
            }, 300);
        }
    };
    var _0xe8e3x7 = {
        run: function() {
            $('#fwslider .timer:eq(' + _0xe8e3x2['cs'] + ') .progress')['animate']({
                width: '100%'
            }, {
                queue: false,
                duration: (_0xe8e3x2['pause'] - (_0xe8e3x2['pause'] / 100) * ((($('#fwslider .timer:eq(' + _0xe8e3x2['cs'] + ') .progress')['width']() / $('#fwslider .timer:eq(' + _0xe8e3x2['cs'] + ')')['width']()) * 100))),
                easing: 'linear',
                complete: function() {
                    $('#fwslider .slideNext')['trigger']('click');
                }
            });
        },
        focus: function() {
            $('#fwslider .slide_content')['on']('mouseover', function() {
                if ($('#fwslider .slide')['is'](':animated')) {
                    return;
                };
                $('#fwslider .timer .progress')['stop']();
            });
            $('#fwslider .slide_content')['on']('mouseleave', function() {
                if ($('#fwslider .slide')['is'](':animated')) {
                    return;
                };
                _0xe8e3x7['run']();
            });
        }
    };
};
$(window)['load'](function() {
    new mainSlider()['init']();
});