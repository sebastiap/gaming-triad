package utils;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import practice.Protagonista;

public class Log {

        private static final Logger logger = LogManager.getLogger(Log.class);

        public static void main() {

            Protagonista prota = new Protagonista("Josef",0,100,"Joestar");
            logger.fatal(prota.presentarse());
            logger.debug("Hello from Log4j 2");
            logger.warn("Esto es una Albertencia");
            logger.info("Esto es una Info inutil");
            logger.error("Este es un error Falso");
            logger.fatal("Estoy Fatal");

            // in old days, we need to check the log level to increase performance
        /*if (logger.isDebugEnabled()) {
            logger.debug("{}", getNumber());
        }*/

            // with Java 8, we can do this, no need to check the log level
            logger.debug("{}", () -> getNumber());

        }

        static int getNumber() {
            return 5;
        }

    }

