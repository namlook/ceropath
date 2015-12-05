
export default {
    widgets: [
        {
            columns: 12,
            type: 'container',
            label: 'Body weight',
            widgets: [
                {
                    type: 'container',
                    columns: 3,
                    widgets: [
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'average (g)',
                                aggregator: {
                                    x: {$avg: 'bodyWeight'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'weight',
                                        suffix: 'g'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'min (g)',
                                aggregator: {
                                    x: {$min: 'bodyWeight'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'weight',
                                        suffix: 'g'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'max (g)',
                                aggregator: {
                                    x: {$max: 'bodyWeight'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'weight',
                                        suffix: 'g'
                                    }
                                }
                            }
                        }
                    ]
                },
                {
                    columns: 9,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomyID': '${_id}'},
                    widget: {
                        type: 'collection-aggregation',
                        label: 'distribution across individuals',
                        aggregator: {
                            x: 'bodyWeight',
                            y: {$count: true}
                        },
                        options: {sort: 'x'},
                        display: {
                            as: 'column',
                            x: {
                                as: 'x',
                                title: 'body weight',
                                suffix: 'g'
                            },
                            y: {
                                as: 'y',
                                title: 'number of individuals'
                                // suffix: 'g'
                            }
                        }
                    }
                }
            ]
        },
        {
            columns: 12,
            type: 'container',
            label: 'Head+body size',
            widgets: [
                {
                    type: 'container',
                    columns: 3,
                    widgets: [
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'average (mm)',
                                aggregator: {
                                    x: {$avg: 'headBodyMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'head+body size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'min (mm)',
                                aggregator: {
                                    x: {$min: 'headBodyMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'head+body size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'max (mm)',
                                aggregator: {
                                    x: {$max: 'headBodyMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'head+body size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        }
                    ]
                },
                {
                    columns: 9,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomyID': '${_id}'},
                    widget: {
                        type: 'collection-aggregation',
                        label: 'distribution across individuals',
                        aggregator: {
                            x: 'headBodyMeasurement',
                            y: {$count: true}
                        },
                        options: {sort: 'x'},
                        display: {
                            as: 'column',
                            x: {
                                as: 'x',
                                title: 'head+body',
                                suffix: 'mm'
                            },
                            y: {
                                as: 'y',
                                title: 'number of individuals'
                                // suffix: 'g'
                            }
                        }
                    }
                }
            ]
        },
        {
            columns: 12,
            type: 'container',
            label: 'Tail size',
            widgets: [
                {
                    type: 'container',
                    columns: 3,
                    widgets: [
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'average (mm)',
                                aggregator: {
                                    x: {$avg: 'tailMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'tail size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'min (mm)',
                                aggregator: {
                                    x: {$min: 'tailMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'tail size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'max (mm)',
                                aggregator: {
                                    x: {$max: 'tailMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'tail size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        }
                    ]
                },
                {
                    columns: 9,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomyID': '${_id}'},
                    widget: {
                        type: 'collection-aggregation',
                        label: 'distribution across individuals',
                        aggregator: {
                            x: 'tailMeasurement',
                            y: {$count: true}
                        },
                        options: {sort: 'x'},
                        display: {
                            as: 'column',
                            x: {
                                as: 'x',
                                title: 'tail size',
                                suffix: 'mm'
                            },
                            y: {
                                as: 'y',
                                title: 'number of individuals'
                                // suffix: 'g'
                            }
                        }
                    }
                },
            ]
        },
        {
            columns: 12,
            type: 'container',
            label: 'Head size',
            widgets: [
                {
                    type: 'container',
                    columns: 3,
                    widgets: [
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'average (mm)',
                                aggregator: {
                                    x: {$avg: 'headMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'head size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'min (mm)',
                                aggregator: {
                                    x: {$min: 'headMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'head size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'max (mm)',
                                aggregator: {
                                    x: {$max: 'headMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'head size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        }
                    ]
                },
                {
                    columns: 9,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomyID': '${_id}'},
                    widget: {
                        type: 'collection-aggregation',
                        label: 'distribution across individuals',
                        aggregator: {
                            x: 'headMeasurement',
                            y: {$count: true}
                        },
                        options: {sort: 'x'},
                        display: {
                            as: 'column',
                            x: {
                                as: 'x',
                                title: 'head',
                                suffix: 'mm'
                            },
                            y: {
                                as: 'y',
                                title: 'number of individuals'
                                // suffix: 'g'
                            }
                        }
                    }
                }
            ]
        },
        {
            columns: 12,
            type: 'container',
            label: 'Hindfoot size',
            widgets: [
                {
                    type: 'container',
                    columns: 3,
                    widgets: [
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'average (mm)',
                                aggregator: {
                                    x: {$avg: 'hindfootMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'hindfoot size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'min (mm)',
                                aggregator: {
                                    x: {$min: 'hindfootMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'hindfoot size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        },
                        {
                            type: 'model-embedded-collection-widget',
                            resource: 'individual',
                            query: {'taxonomyID': '${_id}'},
                            widget: {
                                type: 'collection-aggregation',
                                label: 'max (mm)',
                                aggregator: {
                                    x: {$max: 'hindfootMeasurement'}
                                },
                                display: {
                                    as: 'number',
                                    x: {
                                        as: 'x',
                                        title: 'hindfoot size',
                                        suffix: 'mm'
                                    }
                                }
                            }
                        }
                    ]
                },
                {
                    columns: 9,
                    type: 'model-embedded-collection-widget',
                    resource: 'individual',
                    query: {'taxonomyID': '${_id}'},
                    widget: {
                        type: 'collection-aggregation',
                        label: 'distribution across individuals',
                        aggregator: {
                            x: 'hindfootMeasurement',
                            y: {$count: true}
                        },
                        options: {sort: 'x'},
                        display: {
                            as: 'column',
                            x: {
                                as: 'x',
                                title: 'hindfoot',
                                suffix: 'mm'
                            },
                            y: {
                                as: 'y',
                                title: 'number of individuals'
                                // suffix: 'g'
                            }
                        }
                    }
                }
            ]
        },
    ]
};