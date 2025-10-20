from __future__ import division


class ConfigurationBase(object):
    """
    Base class for all configurations.
    """
    defaults = {}

    def __init__(self, conf, context):
        """
        :param conf: the configuration part for this configurator
        :param context: the complete proxy configuration
        :type context: config.configuration.proxy.ProxyConfiguration
        """
        self.conf = conf
        self.context = context
        for k, v in self.defaults.items():
            if k not in self.conf:
                self.conf[k] = v
