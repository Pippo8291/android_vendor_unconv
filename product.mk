VENDOR_EXTRA_PATH := vendor/extra

$(call inherit-product-if-exists, external/google-fonts/lato/fonts.mk)
$(call inherit-product-if-exists, external/google-fonts/rubik/fonts.mk)
$(call inherit-product-if-exists, external/jetbrainsmono/fonts.mk)

# Custom packages
PRODUCT_PACKAGES += \
    Recorder \
    Terminal

# Extra overlays
PRODUCT_PACKAGE_OVERLAYS += $(VENDOR_EXTRA_PATH)/overlay/common

# Allow overlays to be excluded from enforcing RRO
PRODUCT_ENFORCE_RRO_EXCLUDED_OVERLAYS += $(VENDOR_EXTRA_PATH)/overlay/common

# Extra Font Overlays
# Add a check to avoid duplicate addition other one comes from vendor/lineage/config/common_mobile_full.mk
ifneq ($(filter FontLatoOverlay, $(PRODUCT_PACKAGES)), FontLatoOverlay)
    PRODUCT_PACKAGES += \
        FontJetBrainsMono \
        FontLatoOverlay \
        FontRubikOverlay
endif

# Add font families to fonts-customization.xml
ADDITIONAL_FONTS_FILE += \
   vendor/extra/fonts/fonts-unconv.xml

# Exclude some undesired packages
PRODUCT_PACKAGES += \
    NukePackages

# Some theming overlays
PRODUCT_PACKAGES += \
   CornerRadius-Moar_Round

# Add some nostalgic tunes
PRODUCT_COPY_FILES += \
    frameworks/base/data/sounds/ringtones/ogg/Dione_48k.ogg:$(TARGET_COPY_OUT_PRODUCT)/media/audio/ringtones/Unconv.ogg
